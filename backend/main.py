# main.py - FastAPI app serving prediction endpoint

from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict

app = FastAPI()

# Define input schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Prediction endpoint
@app.post("/predict")
def get_prediction(data: IrisInput):
    input_data = [
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]
    result = predict(input_data)
    return {"predicted_class": result}
