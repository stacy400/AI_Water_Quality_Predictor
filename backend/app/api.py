import os
import pickle
import numpy as np
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class WaterDataInput(BaseModel):
    ph: float
    hardness: float
    solids: float
    chloramines: float
    sulfate: float
    conductivity: float
    organic_carbon: float
    trihalomethanes: float
    turbidity: float

# Load model from ML folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # backend/app -> backend
model_path = os.path.join(BASE_DIR, "..", "ML", "model.pkl")
scaler_path = os.path.join(BASE_DIR, "..", "ML", "scaler.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)
with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

@router.post("/predict")
def predict(data: WaterDataInput):
    input_values = np.array([[data.ph, data.hardness, data.solids, data.chloramines,
                              data.sulfate, data.conductivity, data.organic_carbon,
                              data.trihalomethanes, data.turbidity]])
    input_scaled = scaler.transform(input_values)
    potability = int(model.predict(input_scaled)[0])
    confidence = float(max(model.predict_proba(input_scaled)[0]))
    return {"potability": potability, "confidence": confidence}
