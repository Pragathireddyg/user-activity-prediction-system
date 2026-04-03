from fastapi import FastAPI
import joblib

app = FastAPI()

# Load model
model = joblib.load("model/model.pkl")

@app.get("/")
def home():
    return {"message": "User Engagement Prediction API"}

@app.get("/predict")
def predict(posts: int, reactions: int, days_active: int):
    data = [[posts, reactions, days_active]]
    prediction = model.predict(data)

    return {
        "prediction": int(prediction[0]),
        "result": "Active" if prediction[0] == 1 else "Not Active"
    }