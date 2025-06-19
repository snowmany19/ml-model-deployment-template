# Dockerfile - Containerize the FastAPI app

FROM python:3.10-slim

WORKDIR /app
COPY backend/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Automatically train model
RUN python train.py

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

