# 🗣️ Hate Speech Detection Web App

## 📘 Overview
This project is a **Flask-based web application** that detects **hate speech, offensive language, or safe text** using a trained Machine Learning model and Natural Language Processing (NLP).  
It helps identify harmful or abusive text on social media or chat platforms.

---

## 🎯 Objective
To develop a text classification system that automatically detects hate speech or offensive content using ML and NLP techniques.

---

## ⚙️ Technologies Used

### 🧠 Machine Learning & NLP
- **scikit-learn** – Model training and prediction  
- **NLTK** – Tokenization, stopword removal, and stemming  
- **TF-IDF Vectorizer** – Text feature extraction  
- **Pickle** – Model and vectorizer serialization  

### 💻 Web Framework
- **Flask** – Web application backend  
- **HTML/CSS** – User interface  
- **Jinja2** – Dynamic template rendering  

---
HATESPEECH/
│
├── static/
│ └── style.css # Frontend styling
│
├── templates/
│ └── index.html # Web interface for user input and results
│
├── app.py # Main Flask application
├── model.pkl # Trained ML model for hate speech detection
├── vectorizer.pkl # TF-IDF vectorizer used for text features
├── requirements.txt # Dependencies
└── README.md # Documentation

---

## 🧠 Model Description

The model was trained on a **hate speech dataset** containing labeled tweets and comments categorized as:
- `Hatespeech`
- `Offensive Language`
- `Safe / Neutral`

### 🔍 Preprocessing Steps:
1. Convert text to lowercase  
2. Remove URLs, numbers, HTML tags, and punctuation  
3. Remove stopwords using NLTK  
4. Apply stemming using PorterStemmer  
5. Transform cleaned text into TF-IDF vectors  

### ⚙️ Algorithms (Possible choices)
- Logistic Regression  
- Naive Bayes  
- SVM (Support Vector Machine)

---

## 🧮 How It Works
1. User enters text in the web form.  
2. The text is cleaned (stopword removal, stemming, etc.).  
3. Text is converted to a numeric vector using the TF-IDF model.  
4. The ML model predicts whether the text is:
   - ✅ **Safe Text**
   - ❌ **Offensive Language**
   - ❌ **Hatespeech**
5. Result is displayed instantly on the same page.

---

## 🚀 Steps to Run Locally

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt


## 🧱 Project Structure
