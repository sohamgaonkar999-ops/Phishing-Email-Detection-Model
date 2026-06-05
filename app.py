
from flask import Flask, render_template, request
import joblib
import re

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('phishing_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Clean text function

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', ' URL ', text)
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# Detect suspicious URLs

def url_analysis(text):
    suspicious_words = [
        'verify',
        'login',
        'update',
        'bank',
        'secure',
        'password',
        'urgent',
        'click',
        'free',
        'winner'
    ]

    score = 0

    for word in suspicious_words:
        if word in text.lower():
            score += 1

    return score

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    confidence = None
    danger_score = None

    if request.method == 'POST':
        email_text = request.form['email']

        cleaned = clean_text(email_text)
        vectorized = vectorizer.transform([cleaned])

        result = model.predict(vectorized)[0]
        probabilities = model.predict_proba(vectorized)[0]

        confidence = round(max(probabilities) * 100, 2)
        danger_score = url_analysis(email_text)

        if result == 'phishing':
            prediction = '⚠️ PHISHING EMAIL DETECTED'
        else:
            prediction = '✅ SAFE EMAIL'

    return render_template(
        'index.html',
        prediction=prediction,
        confidence=confidence,
        danger_score=danger_score
    )

if __name__ == '__main__':
    app.run(debug=True)