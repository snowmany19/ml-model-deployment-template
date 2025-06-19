# 🧠 ML Model Deployment Template

A production-ready FastAPI service for serving predictions from a trained RandomForestClassifier on the Iris dataset.

## 🔧 Features
- 🧠 Simple ML model (Random Forest on Iris dataset)
- 🚀 FastAPI REST endpoint for `/predict`
- 🐳 Dockerfile for easy containerization
- 🔄 GitHub Actions CI for training
- 📦 Requirements.txt for dependency management

## 📈 How to Use

### 1. Train the model
```bash
cd backend
python train.py
```

### 2. Run the API
```bash
uvicorn main:app --reload
```

### 3. Use the endpoint
POST `/predict` with JSON:
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### 4. Docker
```bash
docker build -t iris-api .
docker run -p 8000:8000 iris-api
```

## 🧪 Test Script
```python
import requests

data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

response = requests.post("http://localhost:8000/predict", json=data)
print(response.json())
```

## 📂 Structure
- `backend/train.py` — Train and save model
- `backend/predict.py` — Load model and predict
- `backend/main.py` — API server
- `.github/workflows/ci.yml` — CI pipeline
