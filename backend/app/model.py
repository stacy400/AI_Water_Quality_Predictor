import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../../ML/model.pkl")
SCALER_PATH = os.path.join(os.path.dirname(__file__), "../../ML/scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
