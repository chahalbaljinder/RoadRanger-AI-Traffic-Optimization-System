import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler
import numpy as np

# Function to train the traffic model
def train_traffic_model(data):
    # Convert 'time_of_day' from 'HH:MM:SS' to total seconds
    data['time_of_day'] = pd.to_timedelta(data['time_of_day']).dt.total_seconds()

    # Convert 'date' to datetime, then extract year, month, and day as separate features
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data.drop(columns=['date'], inplace=True)  # Drop the original 'date' column

    # One-hot encode categorical columns
    categorical_columns = ['day_of_week', 'Is_Holiday', 'Weather_Condition']
    data = pd.get_dummies(data, columns=categorical_columns)

    # Drop any rows with NaN values that may have resulted from coercion
    data.dropna(inplace=True)

    # Debug: Check if data is empty after preprocessing
    if data.empty:
        print("Data is empty after preprocessing. Please check your input data.")
        return None

    # Prepare features and target variable
    X = data.drop(columns=['congestion_level']).values  # Drop target column for features
    y = data['congestion_level'].values  # Target variable

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Scale the target variable separately
    y = y.astype(np.float32).reshape(-1, 1)
    y_scaled = scaler.fit_transform(y).flatten()  # Flatten back to 1D for the model

    # Reshape X for LSTM input (samples, timesteps, features)
    timesteps = 1  # Example: using a single timestep
    num_features = X_scaled.shape[1]  # Number of features from your dataset
    X_scaled = X_scaled.reshape((X_scaled.shape[0], timesteps, num_features))

    # Define the model
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(timesteps, num_features)))
    model.add(Dropout(0.2))
    model.add(Dense(1))  # Output layer for regression

    # Compile the model
    model.compile(optimizer=Adam(), loss='mean_squared_error')

    # Train the model
    model.fit(X_scaled, y_scaled, epochs=50, batch_size=32, verbose=1)

    return model

# Load your traffic data
try:
    data = pd.read_csv(r'C:\Users\admin\Desktop\Smart traffic management\dummy_traffic_data.csv')  # Replace with your actual dataset
except FileNotFoundError:
    print("The file 'dummy_traffic_data.csv' was not found. Please check the file path.")
    data = None  # Ensure 'data' is None if the file is not found

if data is not None:
    # Train the model
    model = train_traffic_model(data)

    # Check if the model was created successfully
    if model is not None:
        # Save the trained model for later use
        model.save('traffic_model.h5')
    else:
        print("Model training failed. Please check the input data.")
else:
    print("Data loading failed. Cannot proceed to model training.")
