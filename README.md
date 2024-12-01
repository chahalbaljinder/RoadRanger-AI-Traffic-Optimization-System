
# RoadRanger AI Traffic Optimization System

## Overview
The **RoadRanger AI Traffic Optimization System** is a comprehensive solution to modern traffic challenges. It leverages cutting-edge AI models, real-time data ingestion, and cloud infrastructure to optimize traffic flow, predict congestion, and enhance route planning. The system integrates various modules, datasets, and cloud services to create a scalable and efficient traffic management framework.

---

## Features
- **Traffic Congestion Prediction**: Uses AI/ML models to forecast traffic patterns and congestion levels.
- **Route Optimization**: Recommends optimal vehicle routes based on real-time traffic data.
- **Traffic Signal Control**: Dynamically adjusts traffic signal timings to reduce delays.
- **Vehicle Detection**: Processes CCTV and video feeds to detect and count vehicles in real time.
- **Cloud Integration**: Supports AWS IoT, Kinesis, Lambda, and S3 for seamless data streaming and processing.
- **Data-Driven Insights**: Works with diverse datasets (e.g., IoT sensor data, GPS logs, and traffic graphs).

---

## Project Structure
```
.
├── congestion_prediction.py   # Script for predicting traffic congestion
├── requirements.txt           # Python dependencies for the project
├── route_opt_tester.py        # Tester for route optimization algorithms
├── scaler.pkl                 # Preprocessing scaler (e.g., StandardScaler)
├── traffic_model.h5           # Pre-trained AI model for traffic prediction
├── utils.py                   # Helper utility functions
├── yolov5s.pt                 # YOLOv5 weights for object detection
├── cloud_setup/               # Cloud infrastructure setup scripts
│   ├── setup_iot.py           # Configures AWS IoT
│   ├── setup_kinesis.py       # Sets up AWS Kinesis for data streaming
│   ├── setup_lambda.py        # Configures AWS Lambda
│   └── setup_s3.py            # Sets up AWS S3 for data storage
├── datasets/                  # Traffic and simulation datasets
│   ├── cctv_vehicle_detection.csv  # Vehicle detection data
│   ├── dummy_traffic_data.csv      # Sample traffic data
│   ├── gps_data.csv                # GPS logs
│   ├── gps_data.json               # GPS logs in JSON format
│   ├── iot_sensor_data.csv         # IoT sensor readings
│   ├── traffic_graph.json          # Road network graph
│   ├── traffic_signal_control.csv  # Traffic signal settings
│   └── traffic_training_data.csv   # Training dataset for ML
├── src/                      # Core project scripts
│   ├── data_ingestion.py       # Ingests and preprocesses traffic data
│   ├── traffic_signal_control.py # Logic for signal control
│   ├── video_processing.py     # Processes video feeds for vehicle detection
│   └── ai_models/              # AI model implementations
│       ├── object_detection.py     # YOLOv5-based vehicle detection
│       ├── route_optimization.py   # Route optimization logic
│       └── traffic_prediction.py   # Traffic forecasting logic
└── .gitattributes             # Git repository settings
```

---

## Requirements
Install the required dependencies by running:
```bash
pip install -r requirements.txt
```

### Major Libraries
- **TensorFlow/Keras**: For traffic prediction models.
- **PyTorch**: For YOLOv5 object detection.
- **AWS SDKs**: For interacting with AWS IoT, Kinesis, Lambda, and S3.
- **Pandas/Numpy**: For data manipulation and analysis.

---

## Usage

### 1. Traffic Congestion Prediction
Run the `congestion_prediction.py` script to predict congestion levels:
```bash
python congestion_prediction.py
```

### 2. Route Optimization
Use the `route_opt_tester.py` to simulate route optimization:
```bash
python route_opt_tester.py
```

### 3. Traffic Signal Control
Adjust signal timings dynamically using:
```bash
python src/traffic_signal_control.py
```

### 4. Object Detection
Process video feeds for vehicle detection:
```bash
python src/video_processing.py
```

---

## Cloud Setup
Configure AWS services for real-time data processing:

- **IoT Devices**: Use `cloud_setup/setup_iot.py` to connect IoT sensors.
- **Data Streaming**: Run `cloud_setup/setup_kinesis.py` to stream sensor data.
- **Serverless Functions**: Deploy functions with `cloud_setup/setup_lambda.py`.
- **Storage**: Set up S3 buckets via `cloud_setup/setup_s3.py`.

---

## Datasets
The `datasets/` folder includes:
- **Traffic Data**: IoT sensor readings, GPS logs, and synthetic data.
- **Traffic Graph**: JSON file representing road networks.
- **Training Data**: Datasets for machine learning models.

---

## AI Models
- **YOLOv5**: Detects vehicles in video feeds (`yolov5s.pt`).
- **Traffic Prediction**: TensorFlow-based model (`traffic_model.h5`).
- **Route Optimization**: Implements algorithms like Dijkstra or A*.

---

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
