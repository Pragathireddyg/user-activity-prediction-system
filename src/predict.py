import joblib

# Load model
model = joblib.load("model/model.pkl")

# Example input: posts, reactions, days_active
sample = [[10, 50, 15]]

prediction = model.predict(sample)

if prediction[0] == 1:
    print("User will be ACTIVE next week")
else:
    print("User will NOT be active")