from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "Placement Prediction API is running"}

@app.post("/predict")
def predict(cgpa: float, internships: int, projects: int, skills: int):
    data = np.array([[cgpa, internships, projects, skills]])
    prediction = model.predict(data)[0]

    return {"placed": int(prediction)}