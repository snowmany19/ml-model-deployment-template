# train.py - Train and save a RandomForestClassifier on the Iris dataset

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the Iris dataset
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model to disk
joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as model.pkl")
