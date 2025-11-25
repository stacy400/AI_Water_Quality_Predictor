FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt from app folder
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app folder
COPY app ./app


# Expose port
EXPOSE 8000

# Run FastAPI; use PORT env var if provided (Render and other hosts provide $PORT)
# Use shell form so environment variable expansion works
CMD sh -c "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --reload"
