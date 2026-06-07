import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("dataset/network_data.csv")

X = data.drop("attack", axis=1)
y = data["attack"]

model = RandomForestClassifier()

model.fit(X, y)

joblib.dump(model, "models/intrusion_model.pkl")

print("Model Trained")