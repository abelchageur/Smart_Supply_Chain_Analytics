import streamlit as st
import requests

# URL de l'API Cube.js
CUBEJS_API_URL = "http://localhost:4000/cubejs-api/v1/load"
CUBEJS_API_KEY = "your_api_secret"

# Fonction pour interroger Cube.js
def query_cubejs(query):
    headers = {
        "Authorization": f"Bearer {CUBEJS_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(CUBEJS_API_URL, json=query, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error querying Cube.js: {response.text}")

# Requête pour récupérer les KPIs
query = {
    "measures": ["Orders.totalOrders", "Orders.delayedOrders", "Orders.avgDeliveryDuration"]
}

# Récupérer les données
data = query_cubejs(query)

# Extraire les KPIs
total_orders = data["data"][0]["Orders.totalOrders"]
delayed_orders = data["data"][0]["Orders.delayedOrders"]
avg_delivery_duration = data["data"][0]["Orders.avgDeliveryDuration"]

# Afficher les KPIs dans Streamlit
st.title("Logistics KPIs")
st.metric("Total Orders", total_orders)
st.metric("Delayed Orders", delayed_orders)
st.metric("Average Delivery Duration", f"{avg_delivery_duration} days")