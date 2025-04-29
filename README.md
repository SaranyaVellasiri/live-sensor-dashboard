# 🌍 Real-Time Environmental Sensor Dashboard

This project simulates real-time environmental sensor data (Temperature and Humidity) using **Kafka**, stores it into an **Excel** file, and visualizes it live on a **Flask-based** web dashboard.

---

## 🎯 Project Aim

To build a system that:

- Simulates real-time temperature and humidity sensor data.
- Streams the data using Kafka producer and consumer.
- Saves the data continuously to an Excel file.
- Displays the data and live charts on a Flask web dashboard.

---

## 🖼️ Project Preview

✨ Experience the live dashboard in action!  

[▶️ Watch Video](https://drive.google.com/file/d/1lbbNe4jnOeaEC-amoisPeo4yI5rydCI2/view?usp=drive_link)

---

## 🔢 Inputs

The system collects the following sensor data:

- **Area** (North, South, East, West)
- **Timestamp** (Date and Time)
- **Temperature (°C)**
- **Humidity (%)**

Users can filter results on the dashboard by:

- Area
- Date Range (Start and End)
- Time Range (Start and End)

---

## 📤 Outputs

After filtering and processing, the app displays:

- 📈 **Live Average Temperature & Humidity per Area**  
  *(Displayed as a Bar chart using Chart.js)*

- 📊 **Time Series Graph** for selected Area and Time range  
  *(Temperature and Humidity over time)*

---

## 📂 Project Files

- `producer.py` — Kafka producer (generates and sends random sensor data)
- `consumer.py` — Kafka consumer (reads data and saves it into an Excel file)
- `app.py` — Flask application for serving dashboard
- `templates/index.html` — HTML frontend UI
- `sensor_data.xlsx` — Excel file to store all sensor data

---
## 🚀 How to Run the Application 1. **Install dependencies** *(if not already installed)* ```bash pip install flask pandas matplotlib kafka-python openpyxl ``` 2. **Open three separate terminals and run the following commands:** **Terminal 1:** ```bash python producer.py ``` **Terminal 2:** ```bash python consumer.py ``` **Terminal 3:** ```bash python app.py ``` 3. **Then, open your browser and visit:** ```bash http://127.0.0.1:5000/ ``` --- ## 📈 Tech Used ```text Python Flask Apache Kafka Pandas Matplotlib Chart.js Bootstrap 5 (Frontend Styling) ``` --- ## 🌟 Thank You!



