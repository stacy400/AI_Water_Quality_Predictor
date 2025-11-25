# 🚀 Local Development Setup Guide

## Prerequisites
- Python 3.11+
- Node.js 18+
- npm or yarn
- Git

## Option 1: Run with Docker Compose (Recommended - Easiest)

### Step 1: Install Docker
- [Download Docker Desktop](https://www.docker.com/products/docker-desktop)
- Install and start Docker

### Step 2: Run the Application
```bash
cd c:\Users\Admin\Desktop\AI_water_predictor

# Build and start all services
docker-compose up --build

# On first run, this will:
# - Build backend image
# - Build frontend image
# - Start all services
# - Expose ports 3000 (frontend) and 8000 (backend)
```

### Step 3: Access the Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Stop Services
```bash
docker-compose down
```

---

## Option 2: Run Locally Without Docker (For Development)

### Backend Setup

#### Step 1: Create Virtual Environment
```bash
cd backend
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### Step 2: Install Backend Dependencies
```bash
pip install -r app/requirements.txt
```

#### Step 3: Run Backend Server
```bash
cd app
python main.py

# Server will start on http://localhost:8000
# API docs available at http://localhost:8000/docs
```

---

### Frontend Setup (New Terminal)

#### Step 1: Install Frontend Dependencies
```bash
cd frontend
npm install
# or if using yarn
yarn install
```

#### Step 2: Create .env File
```bash
# Create frontend/.env file with:
REACT_APP_API_URL=http://localhost:8000
```

#### Step 3: Start Frontend Development Server
```bash
npm start
# or
yarn start

# Frontend will open at http://localhost:3000
```

---

### ML Training (Optional - New Terminal)

#### Step 1: Set Up ML Environment
```bash
cd ML
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### Step 2: Install ML Dependencies
```bash
pip install -r requirements.txt
```

#### Step 3: Generate Synthetic Data (First Time)
```bash
python dataset_generator.py

# Creates: synthetic_water_data.csv
```

#### Step 4: Train Model
```bash
python train.py

# Creates: model.pkl and scaler.pkl
```

---

## 🧪 Testing the API

### Using cURL (Windows PowerShell):
```powershell
$body = @{
    ph = 7.0
    hardness = 150.0
    solids = 10000.0
    chloramines = 5.0
    sulfate = 300.0
    conductivity = 400.0
    organic_carbon = 10.0
    trihalomethanes = 50.0
    turbidity = 3.5
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/predict" `
  -Method POST `
  -Body $body `
  -ContentType "application/json"
```

### Using Python:
```python
import requests

data = {
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

response = requests.post("http://localhost:8000/predict", json=data)
print(response.json())
```

### Using Swagger UI:
- Go to http://localhost:8000/docs
- Click on the `/predict` endpoint
- Click "Try it out"
- Enter the data
- Click "Execute"

---

## 📁 Project Structure After Setup
```
AI_water_predictor/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api.py
│   │   ├── model.py
│   │   ├── schemas.py
│   │   └── requirements.txt
│   ├── venv/                    # Created after setup
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.js
│   │   ├── index.css
│   │   └── components/
│   │       └── MapView.jsx
│   ├── public/
│   │   └── index.html           # Created after setup
│   ├── node_modules/            # Created after npm install
│   ├── package.json
│   └── Dockerfile
├── ML/
│   ├── train.py
│   ├── dataset_generator.py
│   ├── requirements.txt
│   ├── notebooks/
│   ├── venv/                    # Created after setup
│   ├── model.pkl                # Created after training
│   └── scaler.pkl               # Created after training
├── .github/workflows/
│   └── ci.yml
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── SETUP.md (this file)
```

---

## ⚠️ Common Issues & Solutions

### Port Already in Use
```bash
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process
taskkill /PID <PID> /F

# Or use different port in code
```

### Python Module Not Found
```bash
# Make sure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

### CORS Errors
- Backend already has CORS enabled
- If still having issues, update backend/app/main.py CORS settings

### React Port 3000 in Use
```bash
# Use different port
PORT=3001 npm start
```

---

## 🚀 Before Deployment

### Checklist:
- [ ] Test backend API endpoints with Swagger UI
- [ ] Test frontend connects to backend
- [ ] Environment variables configured
- [ ] .env file created (copy from .env.example)
- [ ] All dependencies installed
- [ ] ML model trained and placed correctly
- [ ] Tests pass
- [ ] Docker images build without errors

### Security Checklist:
- [ ] Change `DEBUG=False` in production
- [ ] Update CORS origins (restrict from "*")
- [ ] Use environment variables for sensitive data
- [ ] Add authentication/authorization if needed
- [ ] Validate all API inputs

---

## 📚 Useful Commands

### Backend
```bash
# Run with auto-reload
uvicorn main:app --reload

# Run with specific host/port
uvicorn main:app --host 0.0.0.0 --port 8001
```

### Frontend
```bash
# Build for production
npm run build

# Run tests
npm test

# Install new package
npm install <package-name>
```

### Docker
```bash
# View logs
docker-compose logs -f

# Remove volumes
docker-compose down -v

# Rebuild specific service
docker-compose build backend
```

---

## 📞 Need Help?

Check the main README.md for more info about the project structure.

Good luck! 🎉
