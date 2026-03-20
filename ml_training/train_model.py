import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("../dataset/cleaned_tickets.csv")

X = data["text"]
y = data["category"]

vectorizer = TfidfVectorizer(stop_words="english")

X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)

model.fit(X_vec,y)

joblib.dump(model,"../trained_model/classifier.pkl")
joblib.dump(vectorizer,"../trained_model/vectorizer.pkl")

print("Model trained successfully")