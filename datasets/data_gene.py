import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta

# Constants
np.random.seed(42)
start_time = datetime(2024, 10, 11, 8, 0, 0)
time_intervals = 1000

# Generate timestamp series
timestamps = [start_time + timedelta(minutes=5 * i) for i in range(time_intervals)]

# 1. IoT Sensor Data
iot_sensor_data = pd.DataFrame({
    'sensor_id': np.random.choice(['sensor_1', 'sensor_2', 'sensor_3'], time_intervals),
    'location': np.random.choice(['Main_Street', 'Second_Street', 'Third_Street'], time_intervals),
    'timestamp': timestamps,
    'vehicle_count': np.random.randint(10, 50, time_intervals),
    'average_speed': np.random.randint(20, 80, time_intervals)
})

# 2. GPS Data
gps_data = pd.DataFrame({
    'vehicle_id': [f'vehicle_{i % 50 + 1}' for i in range(time_intervals)],
    'timestamp': timestamps,
    'latitude': np.random.uniform(40.7120, 40.7150, time_intervals),
    'longitude': np.random.uniform(-74.0100, -74.0050, time_intervals),
    'speed': np.random.randint(20, 80, time_intervals)
})

# 3. CCTV Vehicle Detection
cctv_vehicle_detection = pd.DataFrame({
    'camera_id': np.random.choice(['camera_1', 'camera_2', 'camera_3'], time_intervals),
    'location': np.random.choice(['Downtown_Intersection', 'Uptown_Crossroad', 'City_Hall'], time_intervals),
    'timestamp': timestamps,
    'vehicle_count': np.random.randint(10, 50, time_intervals)
})

# 4. AI Model Training Data
time_of_day = [t.hour for t in timestamps]
day_of_week = [t.weekday() for t in timestamps]
congestion_level = np.random.randint(1, 6, time_intervals)

traffic_training_data = pd.DataFrame({
    'timestamp': timestamps,
    'vehicle_count': iot_sensor_data['vehicle_count'],
    'time_of_day': time_of_day,
    'day_of_week': day_of_week,
    'congestion_level': congestion_level
})

# 5. Traffic Graph
traffic_graph = {
    "nodes": [f"Node_{i}" for i in range(1, 21)],
    "edges": [
        {"from": f"Node_{i}", "to": f"Node_{j}", "traffic": np.random.randint(1, 10)}
        for i in range(1, 21) for j in range(i+1, 21)
    ]
}

# 6. Traffic Signal Control
traffic_signal_control = pd.DataFrame({
    'signal_id': np.random.choice(['signal_1', 'signal_2', 'signal_3'], time_intervals),
    'location': np.random.choice(['Main_Street_Crossing', 'Second_Street_Crossing', 'Third_Street_Crossing'], time_intervals),
    'timestamp': timestamps,
    'green_time': np.random.randint(20, 60, time_intervals),
    'red_time': np.random.randint(20, 60, time_intervals)
})

# Saving the data
iot_sensor_data.to_csv('iot_sensor_data.csv', index=False)
gps_data.to_csv('gps_data.csv', index=False)
cctv_vehicle_detection.to_csv('cctv_vehicle_detection.csv', index=False)
traffic_training_data.to_csv('traffic_training_data.csv', index=False)
traffic_signal_control.to_csv('traffic_signal_control.csv', index=False)

with open('traffic_graph.json', 'w') as f:
    json.dump(traffic_graph, f, indent=4)

"Sample files have been created and saved."
