from flask import Flask, render_template, request
import pickle
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Setup
app = Flask(__name__)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Text cleaning function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    
    # Remove stopwords
    words = [word for word in text.split() if word not in stop_words]
    
    # Apply stemming
    stemmed_words = [stemmer.stem(word) for word in words]
    
    return " ".join(stemmed_words)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]

    if prediction == "Offensive Language":
        result = "❌ OFFENSIVE"
    elif prediction == "Hatespeech":
        result = "❌ Hatespeech"
    else:
        result = "✅ Safe Text"

    return render_template('index.html', prediction=result, input_text=text)

if __name__ == '__main__':
    app.run(debug=True)
