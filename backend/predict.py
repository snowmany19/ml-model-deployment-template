# predict.py - Load the trained model and return predictions

import joblib
import os

def load_model():
    # Ensure model loads relative to this file’s directory
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    return joblib.load(model_path)

def predict(input_data):
    model = load_model()
    return model.predict([input_data])[0]

