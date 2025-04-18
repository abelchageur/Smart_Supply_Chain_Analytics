    from kafka import KafkaConsumer
    import json
    import pandas as pd
    import os

    # Kafka Consumer Configuration
    consumer = KafkaConsumer(
        'csv_topic',  # Topic name
        bootstrap_servers='kafka:9092',  # Kafka broker address
        auto_offset_reset='earliest',  # Start reading at the earliest message
        enable_auto_commit=True,  # Automatically commit offsets
        group_id='my-group',  # Consumer group ID
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON messages
    )

    # Path to the dbt seeds directory
    SEEDS_DIR = "/home/appuser/seeds"  # Replace with the actual path to your dbt seeds directory
    CSV_FILE = os.path.join(SEEDS_DIR, "data.csv")

    # Function to append data to a CSV file
    def append_to_csv(data, csv_file):
        df = pd.DataFrame([data])
        
        # Replace NaN values with None (for compatibility with Snowflake NULLs)
        df = df.where(pd.notnull(df), None)
        
        if os.path.exists(csv_file):
            # Append to existing CSV file
            df.to_csv(csv_file, mode='a', header=False, index=False)
        else:
            # Create a new CSV file with headers
            df.to_csv(csv_file, mode='w', header=True, index=False)
        print(f"Data appended to {csv_file}")

    # Main Consumer Loop
    if __name__ == "__main__":
        print("Starting Kafka consumer...")
        
        # Ensure the seeds directory exists
        os.makedirs(SEEDS_DIR, exist_ok=True)
        
        # Start consuming messages from Kafka
        for message in consumer:
            data = message.value  # Extract the JSON data from the Kafka message
            print("Received data:", data)
            
            # Append the data to the CSV file
            append_to_csv(data, CSV_FILE)