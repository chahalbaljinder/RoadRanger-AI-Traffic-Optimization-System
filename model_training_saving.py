import pandas as pd
from src.ai_models.traffic_prediction import train_traffic_model

# Load your traffic data
data = pd.read_csv(r'C:\Users\admin\Desktop\Smart traffic management\dummy_traffic_data.csv')  # Replace with your actual dataset

# Train the model
model = train_traffic_model(data)

# Save the trained model for later use
model.save('traffic_model.h5')