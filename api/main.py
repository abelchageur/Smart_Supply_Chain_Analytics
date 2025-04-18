# from fastapi import FastAPI
# from kafka import KafkaProducer
# import pandas as pd
# import time
# import json

# app = FastAPI()
# producer = KafkaProducer(
#     bootstrap_servers='kafka:9092',
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

# @app.get("/")
# def root():
#     return {"message": "API for CSV Ingestion to Kafka"}

# @app.post("/ingest_csv/")
# def ingest_csv():
#     try:
#         df = pd.read_csv('/app/data/DataCoSupplyChainDataset.csv', encoding='latin1')  # chemin dans container
#         total_rows = len(df)
#         chunk_size = 1000  # Adjust the chunk size to control how many rows are sent in each chunk
        
#         # Loop through the data in chunks
#         for start_row in range(0, total_rows, chunk_size):
#             end_row = min(start_row + chunk_size, total_rows)
#             chunk = df.iloc[start_row:end_row]
            
#             # Send each row in the chunk to Kafka
#             for _, row in chunk.iterrows():
#                 producer.send('csv_topic', row.to_dict())

#             producer.flush()  # Flush after sending each chunk

#             # Wait for 3 minutes before sending the next chunk
#             time.sleep(120)  # 180 seconds = 3 minutes

#         return {"message": "CSV sent to Kafka in chunks"}

#     except Exception as e:
#         return {"error": str(e)}
from fastapi import FastAPI
from kafka import KafkaProducer
import pandas as pd
import time
import json

app = FastAPI()

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.get("/")
def root():
    return {"message": "API for CSV Ingestion to Kafka"}

@app.post("/ingest_csv/")
def ingest_csv():
    try:
        # Read the CSV file
        df = pd.read_csv('/app/data/DataCoSupplyChainDataset.csv', encoding='latin1')  # Path inside the container
        
        # Iterate through each row in the DataFrame
        for _, row in df.iterrows():
            # Send the row as a dictionary to Kafka
            producer.send('csv_topic', row.to_dict())
            
            # Flush the producer to ensure the message is sent immediately
            producer.flush()
            
            # Wait for 0.5 seconds before sending the next row
            time.sleep(0.5)

        return {"message": "CSV sent to Kafka row by row"}

    except Exception as e:
        return {"error": str(e)}