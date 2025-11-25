from fastapi import APIRouter
from app.schemas import WaterDataInput, PredictionOutput
from app.model import predict_potability

router = APIRouter()

@router.post("/predict", response_model=PredictionOutput)
async def predict(data: WaterDataInput):
    """
    Predict water potability based on input features.
    """
    prediction = predict_potability(data)
    return prediction

@router.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy"}
