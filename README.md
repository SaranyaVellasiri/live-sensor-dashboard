🌍 Real-Time Environmental Sensor Dashboard
This project simulates real-time environmental sensor data (Temperature and Humidity) using Kafka, stores it into an Excel file, and visualizes it live on a Flask-based web dashboard.

🎯 Project Aim
To build a system that:

Simulates real-time temperature and humidity sensor data.

Streams the data using Kafka producer and consumer.

Saves the data continuously to an Excel file.

Displays the data and live charts on a Flask web dashboard.

🖼️ Project Preview
✨ Experience the live dashboard in action! Watch the full video below:
  
[▶️ Watch Video](./video/LiveSensorDashboard.mp4)


[▶️ Watch Video on Google Drive](https://drive.google.com/file/d/1BGETejhtTfwsCahZP-I10SclmZK7lAVl/view?usp=drive_link)


🔢 Inputs
The system collects the following sensor data:

Area (North, South, East, West)

Timestamp (Date and time)

Temperature (°C)

Humidity (%)

Users can filter results on the dashboard by:

Area

Date Range (Start and End)

Time Range (Start and End)

📤 Outputs
After filtering and processing, the app displays:

📈 Live Average Temperature & Humidity per Area (Bar chart using Chart.js)

📊 Time Series Graph for selected Area and Time range (Temperature and Humidity over time)

📂 Project Files
producer.py — Kafka producer (generates and sends random sensor data)

consumer.py — Kafka consumer (reads data and saves it into an Excel file)

app.py — Flask application for serving dashboard

templates/index.html — HTML frontend UI

sensor_data.xlsx — Excel file to store all sensor data

🚀 How to Run
Start Kafka and Zookeeper services on your machine.

Install dependencies:

bash
Copy
Edit
pip install flask pandas matplotlib kafka-python openpyxl
In separate terminals, run the following:

bash
Copy
Edit
python producer.py
python consumer.py
python app.py
Open your browser and visit:

cpp
Copy
Edit
http://127.0.0.1:5000/
📈 Tech Used
Python

Flask

Apache Kafka

Pandas

Matplotlib

Chart.js

Bootstrap 5 (Frontend Styling)

🌟 Thank You!
