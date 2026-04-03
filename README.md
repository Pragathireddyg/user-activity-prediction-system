 User Activity Prediction System 

This project is a simple end-to-end machine learning pipeline that predicts whether a user will be active in the next week based on their recent activity.

I built this to understand how user engagement signals (like posts and reactions) can be used to model retention, and how to expose an ML model through a production-style API.




The system takes in basic user activity metrics:
- Number of posts
- Number of reactions
- Number of active days

Using these features, a trained machine learning model predicts whether the user is likely to be active in the following week.

The model is served through a FastAPI backend, allowing real-time predictions via API calls.



- Algorithm: Random Forest Classifier
- Input features:
  - `posts`
  - `reactions`
  - `days_active`
- Target:
  - `active_next_week` (0 or 1)

The dataset used in this project is synthetically generated to simulate user behavior patterns.



How did I run?

 1. Install dependencies
```bash
pip install fastapi uvicorn pandas scikit-learn matplotlib
```

 2. Train the model
```bash
python src/train_model.py
```

 3. Start the API server
```bash
uvicorn api.main:app --reload
```

---

API
Once the server is running, open:

http://127.0.0.1:8000/docs

You can test the endpoint directly from Swagger UI.

 Example request:
```
/predict?posts=10&reactions=50&days_active=15
```

Example response:
```json
{
  "prediction": 1,
  "result": "Active"
}
```

---

Project Structureeeeeeeee

```
api/
  main.py

src/
  data_processing.py
  eda.py
  train_model.py
  predict.py
```



What I Focused On

- Building a clean ML pipeline (data → model → prediction)
- Understanding how feature values influence user retention
- Exposing the model via an API instead of just a notebook
- Structuring the project in a modular way



 Notesssssss

- The dataset is synthetic and meant for experimentation.
- The model can be improved further with real-world data and feature engineering.


 Future Improvements....might do

- Use real user engagement data
- Add model evaluation metrics
- Deploy the API
- Add frontend dashboard


 Techhhhhhhh Stack

- Python
- Pandas / NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Matplotlib
