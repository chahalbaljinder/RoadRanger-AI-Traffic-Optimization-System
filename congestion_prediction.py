from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the trained model
model = load_model('traffic_model.h5')

# Define input data with only 18 features (ensure it matches the training feature count and order)
input_data = {
    'vehicle_count': [35],           # Example vehicle count
    'time_of_day': [14 * 3600],      # Example time in seconds
    'day_of_week_Monday': [0],       # One-hot encode day of the week
    'day_of_week_Tuesday': [0],
    'day_of_week_Wednesday': [0],
    'day_of_week_Thursday': [0],
    'day_of_week_Friday': [0],
    'day_of_week_Saturday': [0],
    'day_of_week_Sunday': [1],       # Example: 1 if Sunday
    'Is_Holiday_No': [1],            # 1 if not a holiday, 0 otherwise
    'Is_Holiday_Yes': [0],
    'Weather_Condition_Clear': [1],  # One-hot encoded weather condition
    'Weather_Condition_Rain': [0],
    'Weather_Condition_Snow': [0],
    'Weather_Condition_Fog': [0],
    'Avg_Speed': [45],               # Example average speed
    'month': [1],
    'day': [1]
}

# Convert input data to DataFrame
new_data_df = pd.DataFrame(input_data)

# Ensure StandardScaler is fitted with consistent feature structure
scaler = StandardScaler()
dummy_data = pd.DataFrame(np.zeros((1, 18)), columns=new_data_df.columns)  # 18 features
scaler.fit(dummy_data)  # Fit scaler on dummy data with same feature count

# Scale input data
new_data_scaled = scaler.transform(new_data_df)

# Reshape data for LSTM input (samples, timesteps, features)
new_data_reshaped = new_data_scaled.reshape((1, 1, new_data_scaled.shape[1]))

# Make predictions
prediction = model.predict(new_data_reshaped)

# Output the predicted congestion level
print("Predicted Congestion Level:", prediction[0][0])
