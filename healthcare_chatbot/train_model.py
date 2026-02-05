import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

print("Loading processed dataset...")

df = pd.read_csv("processed_dataset.csv")

# ✅ Correct column names
X = df["symptoms_text"]
y = df["disease"]

print("Vectorizing text...")
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

print("Training model...")
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

# Save model & vectorizer for OFFLINE use
joblib.dump(model, "disease_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model trained and saved successfully")
