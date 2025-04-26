from flask import Flask, render_template, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import os

app = Flask(__name__)

# Load sensor data CSV
DATA_PATH = 'sensor_data.xlsx'

def load_data():
    df = pd.read_excel(DATA_PATH)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.columns = df.columns.str.strip().str.lower()  # normalize columns
    return df

# Route for Home Page
@app.route('/', methods=['GET', 'POST'])
def index():
    data = load_data()
    graph1 = None

    if request.method == 'POST':
        area = request.form['area']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        # Filter by area and datetime
        data['date'] = data['timestamp'].dt.date.astype(str)
        data['time'] = data['timestamp'].dt.time.astype(str)

        filtered_data = data[
            (data['area'] == area) &
            (data['date'] >= start_date) &
            (data['date'] <= end_date) &
            (data['time'] >= start_time) &
            (data['time'] <= end_time)
        ]

        if not filtered_data.empty:
            fig, ax1 = plt.subplots(figsize=(10, 4))
            ax1.plot(filtered_data['timestamp'], filtered_data['temperature'], color='red', label='Temperature (°C)')
            ax1.set_ylabel('Temperature (°C)', color='red')
            ax1.tick_params(axis='y', labelcolor='red')

            ax2 = ax1.twinx()
            ax2.plot(filtered_data['timestamp'], filtered_data['humidity'], color='blue', label='Humidity (%)')
            ax2.set_ylabel('Humidity (%)', color='blue')
            ax2.tick_params(axis='y', labelcolor='blue')

            plt.title(f"{area} Area - Temp & Humidity Over Time")
            fig.tight_layout()

            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.getvalue()).decode()
            graph1 = image_base64
            plt.close()

    return render_template('index.html', graph1=graph1)

# 🔁 JSON API Route for Chart.js Auto Refresh
@app.route('/average')
def average_data():
    data = load_data()
    avg_data = data.groupby('area').agg({'temperature': 'mean', 'humidity': 'mean'}).reset_index()

    return jsonify({
        'areas': avg_data['area'].tolist(),
        'temperature': [round(t, 2) for t in avg_data['temperature']],
        'humidity': [round(h, 2) for h in avg_data['humidity']]
    })

if __name__ == '__main__':
    if not os.path.exists(DATA_PATH):
        print(f"Error: {DATA_PATH} not found!")
    else:
        app.run(debug=True)
