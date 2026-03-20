import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model = joblib.load(os.path.join(BASE_DIR,"../trained_model/classifier.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR,"../trained_model/vectorizer.pkl"))

def predict_category(text):

    X = vectorizer.transform([text])

    return model.predict(X)[0]