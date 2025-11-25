import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle

def load_data(filepath):
    """Load water potability dataset."""
    df = pd.read_csv(filepath)
    return df

def preprocess_data(df):
    """Preprocess the dataset."""
    # Handle missing values
    df = df.dropna()
    
    # Separate features and target
    X = df.drop('Potability', axis=1)
    y = df['Potability']
    
    return X, y

def train_model(X, y):
    """Train the machine learning model."""
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate
    score = model.score(X_test_scaled, y_test)
    print(f"Model Accuracy: {score:.4f}")
    
    return model, scaler

if __name__ == "__main__":
    df = load_data("water_potability.csv")
    X, y = preprocess_data(df)
    model, scaler = train_model(X, y)
    
    # Save model
    pickle.dump(model, open("model.pkl", "wb"))
    pickle.dump(scaler, open("scaler.pkl", "wb"))
    print("Model saved!")
