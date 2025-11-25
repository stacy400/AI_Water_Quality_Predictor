import os
import pickle
import logging
import numpy as np
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

logger = logging.getLogger("backend.api")
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


# Default model locations (relative to backend folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # backend/app -> backend
DEFAULT_MODEL_PATH = os.path.join(BASE_DIR, "ML", "model.pkl")
DEFAULT_SCALER_PATH = os.path.join(BASE_DIR, "ML", "scaler.pkl")


# Lazy-loaded model and scaler
_model = None
_scaler = None


def load_model_if_needed():
    """Load model and scaler on first use. Returns (model, scaler) or (None, None) if not available."""
    global _model, _scaler
    if _model is not None and _scaler is not None:
        return _model, _scaler

    model_path = os.getenv("MODEL_PATH", DEFAULT_MODEL_PATH)
    scaler_path = os.getenv("SCALER_PATH", DEFAULT_SCALER_PATH)

    try:
        if os.path.exists(model_path) and os.path.exists(scaler_path):
            with open(model_path, "rb") as f:
                _model = pickle.load(f)
            with open(scaler_path, "rb") as f:
                _scaler = pickle.load(f)
            logger.info("Loaded model from %s and scaler from %s", model_path, scaler_path)
            return _model, _scaler
        else:
            logger.warning("Model or scaler not found (model=%s, scaler=%s)", model_path, scaler_path)
            return None, None
    except Exception as exc:
        logger.exception("Error loading model/scaler: %s", exc)
        return None, None


@router.post("/predict")
def predict(data: WaterDataInput):
    model, scaler = load_model_if_needed()
    if model is None or scaler is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=("Model not available. Train the model and provide MODEL_PATH/SCALER_PATH "
                    "environment variables or place model files in the ML/ directory."),
        )

    input_values = np.array([[data.ph, data.hardness, data.solids, data.chloramines,
                              data.sulfate, data.conductivity, data.organic_carbon,
                              data.trihalomethanes, data.turbidity]])
    input_scaled = scaler.transform(input_values)
    potability = int(model.predict(input_scaled)[0])
    # protect against missing predict_proba
    try:
        proba = model.predict_proba(input_scaled)[0]
        confidence = float(max(proba))
    except Exception:
        confidence = 1.0
    return {"potability": potability, "confidence": confidence}
