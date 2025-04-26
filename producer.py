from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

# Kafka server and topics
KAFKA_SERVER = "localhost:9092"
AREAS = {
    "North": "north_topic",
    "South": "south_topic",
    "East": "east_topic",
    "West": "west_topic"
}

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Generate fake temperature and humidity data
def generate_data(area):
    return {
        "area": area,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(30, 70), 2)
    }

# Continuously send data
while True:
    for area, topic in AREAS.items():
        data = generate_data(area)
        producer.send(topic, value=data)
        print(f"Produced to {topic}: {data}")
        time.sleep(1)  # Small delay between areas

    time.sleep(2)  # Delay before next round
