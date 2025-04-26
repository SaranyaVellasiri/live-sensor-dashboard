from kafka import KafkaConsumer
import json
import pandas as pd
import os

# Kafka config
TOPICS = ["north_topic", "south_topic", "east_topic", "west_topic"]
KAFKA_SERVER = "localhost:9092"
EXCEL_FILE = "sensor_data.xlsx"

# Create Kafka consumer
consumer = KafkaConsumer(
    *TOPICS,
    bootstrap_servers=KAFKA_SERVER,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Read existing file or create new DataFrame
if os.path.exists(EXCEL_FILE):
    df_all = pd.read_excel(EXCEL_FILE)
else:
    df_all = pd.DataFrame(columns=["area", "timestamp", "temperature", "humidity"])

print("✅ Kafka Consumer started and waiting for data...")

# Continuously listen for messages and store them
for message in consumer:
    data = message.value
    print(f"Consumed from {message.topic}: {data}")

    new_row = pd.DataFrame([data])
    df_all = pd.concat([df_all, new_row], ignore_index=True)

    # Save to Excel
    df_all.to_excel(EXCEL_FILE, index=False)
