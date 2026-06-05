# 🛡️ Phishing Email Detection Model

A Real-Time Phishing Email Detection System built using **Python**, **Scikit-learn**, and **Flask** that classifies emails as **Phishing** or **Safe** using Machine Learning and URL/Text feature analysis.

---

# 🚀 Features

✅ Real-Time Email Detection  
✅ Machine Learning using Scikit-learn  
✅ URL & Keyword Analysis  
✅ Detects Suspicious Email Content  
✅ Accuracy Score & Confusion Matrix  
✅ Flask Web Interface  
✅ Live Prediction System  
✅ Clean UI Design  
✅ Easy to Run & Customize  

---

# 🧠 Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- TF-IDF Vectorizer
- Logistic Regression
- HTML/CSS

---

# 📂 Project Structure

```bash
Phishing-Email-Detection-Model/
│
├── app.py
├── train_model.py
├── dataset.csv
├── requirements.txt
├── phishing_model.pkl
├── vectorizer.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sohamgaonkar999-ops/Phishing-Email-Detection-Model.git
```

---

## 2️⃣ Open Project Folder

```bash
cd Phishing-Email-Detection-Model
```

---

## 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# 🏋️ Train the Machine Learning Model

Run:

```bash
python train_model.py
```

After successful training:

```bash
Model and vectorizer saved successfully.
```

Generated files:

```bash
phishing_model.pkl
vectorizer.pkl
```

---

# ▶️ Run Real-Time Detection App

Run:

```bash
python app.py
```

You will see:

```bash
Running on http://127.0.0.1:5000
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# 🧪 Example Test Emails

## ⚠️ Phishing Email

```text
Your PayPal account has been suspended.
Click here immediately to verify:
http://paypal-secure-login.xyz
```

Expected Output:

```text
PHISHING EMAIL DETECTED
```

---

## ✅ Safe Email

```text
Hello Team,
Please find attached weekly meeting notes.
Regards
```

Expected Output:

```text
SAFE EMAIL
```

---

# 📊 Model Workflow

1. Email Text Input
2. Text Cleaning & Preprocessing
3. TF-IDF Feature Extraction
4. Machine Learning Prediction
5. URL & Keyword Analysis
6. Final Classification Result

---

# 🔍 Detection Capabilities

The system detects:

- Suspicious URLs
- Fake login requests
- Password reset scams
- Banking phishing attempts
- Urgent action messages
- Free prize scams
- Credential harvesting attempts

---

# 📈 Future Improvements

- Gmail API Integration
- Browser Extension
- Deep Learning (LSTM/BERT)
- Attachment Scanning
- WHOIS Domain Analysis
- Real URL Reputation APIs
- Advanced NLP Models
- Email Header Analysis

---

# 🖥️ Screenshots

## Home Page

- Email Input Box
- Detect Button
- Real-Time Result Display
- Confidence Score
- Danger Score

---

# 🛠️ Requirements

```txt
flask
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn
```

---

# 📌 Simple Run Commands

```bash
pip install -r requirements.txt
python train_model.py
python app.py
```

---

# 🎯 Expected Outcome

The model successfully classifies emails as:

✅ Safe  
⚠️ Phishing  

using textual content, suspicious keywords, and URL analysis with high accuracy.

---

# 📄 License

This project is for educational and research purposes.

---

# 👨‍💻 Author

SOHAM GAONKAR

GitHub Repository:

https://github.com/sohamgaonkar999-ops/Phishing-Email-Detection-Model
