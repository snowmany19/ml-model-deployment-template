# predict.py - Load the trained model and return predictions

import joblib

def load_model():
    return joblib.load("model.pkl")

def predict(input_data):
    model = load_model()
    return model.predict([input_data])[0]
