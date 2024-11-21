import boto3
import csv
import json
import os

# AWS Configuration
KINESIS_STREAM_NAME = "TrafficDataStream"
S3_BUCKET_NAME = "smart-traffic-data"
AWS_REGION = "ap-south-1"

# Create AWS clients
kinesis_client = boto3.client('kinesis', region_name=AWS_REGION)
s3_client = boto3.client('s3', region_name=AWS_REGION)

# AWS Lambda Client for triggering functions
lambda_client = boto3.client('lambda', region_name=AWS_REGION)

# Function to upload to S3
def upload_to_s3(file_path, bucket_name, object_name):
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to S3 bucket {bucket_name} as {object_name}")
    except Exception as e:
        print(f"Error uploading file {file_path}: {e}")

# Function to send records to Kinesis
def send_to_kinesis(record, stream_name=KINESIS_STREAM_NAME):
    try:
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(record),
            PartitionKey=str(record['sensor_id'])
        )
        print(f"Record sent to Kinesis stream: {record}")
    except Exception as e:
        print(f"Error sending record to Kinesis: {e}")

# Function to ingest IoT data (Sensor Data)
def ingest_iot_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            record = {
                'sensor_id': row['sensor_id'],
                'vehicle_count': row['vehicle_count'],
                'timestamp': row['timestamp'],
                'vehicle_count': int(row['vehicle_count']),
                'average_speed': int(row['average_speed'])
            }
            send_to_kinesis(record)
            print(f"Ingested IoT Data: {record}")

# Function to ingest GPS data
def ingest_gps_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            record = {
                'vehicle_id': row['vehicle_id'],
                'timestamp': row['timestamp'],
                'latitude': float(row['latitude']),
                'longitude': float(row['longitude']),
                'speed': int(row['speed'])
            }
            send_to_kinesis(record)
            print(f"Ingested GPS Data: {record}")

# Function to ingest CCTV vehicle detection data
def ingest_cctv_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            record = {
                'camera_id': row['camera_id'],
                'location': row['location'],
                'timestamp': row['timestamp'],
                'vehicle_count': int(row['vehicle_count'])
            }
            send_to_kinesis(record)
            print(f"Ingested CCTV Data: {record}")

# Function to upload AI model training data to S3
def upload_training_data_to_s3(file_path):
    upload_to_s3(file_path, S3_BUCKET_NAME, 'training_data/traffic_training_data.csv')

# Function to upload Traffic Graph JSON to S3
def upload_traffic_graph(file_path):
    upload_to_s3(file_path, S3_BUCKET_NAME, 'traffic_graph/traffic_graph.json')

# Function to adjust traffic signals (Ingest traffic signal control data)
def adjust_traffic_signals(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Process signal control logic (e.g., adjusting signal timings)
            print(f"Adjusting signal {row['signal_id']} at {row['location']} with green_time: {row['green_time']}s, red_time: {row['red_time']}s.")

# Main function to execute data ingestion tasks
def main():
    print("Starting Data Ingestion...")

    # Ingest IoT sensor data
    ingest_iot_data(r'C:\Users\admin\Desktop\Smart traffic management\Smart-Traffic-Management-System\datasets\iot_sensor_data.csv')

    # Ingest GPS data
    ingest_gps_data(r'C:\Users\admin\Desktop\Smart traffic management\Smart-Traffic-Management-System\datasets\gps_data.csv')

    # Ingest CCTV vehicle detection data
    ingest_cctv_data(r'C:\Users\admin\Desktop\Smart traffic management\Smart-Traffic-Management-System\datasets\cctv_vehicle_detection.csv')

    # Upload AI model training data to S3
    upload_training_data_to_s3(r'C:\Users\admin\Desktop\Smart traffic management\Smart-Traffic-Management-System\datasets\dummy_traffic_data.csv')

    # Upload Traffic Graph to S3
    upload_traffic_graph(r'C:\Users\admin\Desktop\Smart traffic management\Smart-Traffic-Management-System\datasets\traffic_graph.json')

    # Adjust traffic signals
    adjust_traffic_signals(r'C:\Users\admin\Desktop\Smart traffic management\Smart-Traffic-Management-System\datasets\traffic_signal_control.csv')

    print("Data Ingestion Completed.")

if __name__ == "__main__":
    main()
