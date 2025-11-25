from pydantic import BaseModel
from typing import Optional

class WaterDataInput(BaseModel):
    """Schema for water quality input data."""
    ph: float
    hardness: float
    solids: float
    chloramines: float
    sulfate: float
    conductivity: float
    organic_carbon: float
    trihalomethanes: float
    turbidity: float

class PredictionOutput(BaseModel):
    """Schema for prediction output."""
    potability: int
    confidence: float
