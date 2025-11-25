# Water Potability Predictor

A machine learning application to predict water potability using water quality metrics.

## Project Structure

```
water_potability_predictor/
├─ backend/
│ ├─ app/
│ │ ├─ main.py
│ │ ├─ api.py
│ │ ├─ model.py
│ │ ├─ schemas.py
│ │ └─ requirements.txt
│ └─ Dockerfile
├─ ml/
│ ├─ notebooks/
│ │ └─ 01_data_cleaning_and_training.ipynb
│ ├─ train.py
│ ├─ dataset_generator.py
│ └─ requirements.txt
├─ frontend/
│ ├─ src/
│ │ ├─ App.jsx
│ │ ├─ components/MapView.jsx
│ │ └─ index.css
│ ├─ package.json
│ └─ Dockerfile
├─ docker-compose.yml
├─ README.md
└─ .github/workflows/ci.yml
```

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Python 3.11+
- Node.js 18+

### Installation

1. Clone the repository
2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

### Backend API
- Base URL: `http://localhost:8000`
- Health Check: `GET /health`
- Predict: `POST /predict`

### Frontend
- Access at: `http://localhost:3000`

## Features
- Water quality prediction using machine learning
- REST API with FastAPI
- Interactive React frontend
- Docker containerization
- CI/CD pipeline ready

## Model Training

To train the model locally:
```bash
cd ml
python train.py
```

## API Documentation

### POST /predict
Predict water potability based on water quality parameters.

**Request Body:**
```json
{
  "ph": 7.0,
  "hardness": 150.0,
  "solids": 10000.0,
  "chloramines": 5.0,
  "sulfate": 300.0,
  "conductivity": 400.0,
  "organic_carbon": 10.0,
  "trihalomethanes": 50.0,
  "turbidity": 3.5
}
```

**Response:**
```json
{
  "potability": 1,
  "confidence": 0.85
}
```

## License
MIT
