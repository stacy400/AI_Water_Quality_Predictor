FROM python:3.10-slim

WORKDIR /app

# Copy requirements from backend/app
COPY backend/app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend/app folder
COPY backend/app .

# Run your backend
CMD ["python", "main.py"]

