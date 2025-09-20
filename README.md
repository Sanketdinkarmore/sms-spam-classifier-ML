# 📩 SMS Spam Classification (Streamlit)

A simple yet effective **SMS/Email spam classifier** using **NLTK** preprocessing and a **scikit-learn model**, served with **Streamlit**.  
This project demonstrates how text preprocessing + machine learning can be combined into an interactive web app.

---

## 🌐 Live Demo
👉 [Try the app here](https://sms-spam-classifier-ml-ekfwxqgxqvtdve6uv5ypwd.streamlit.app/)

---

## 📂 Project Structure
- `app.py` – Streamlit app
- `modle.pkl` – trained classifier
- `vectorizer.pkl` – TF-IDF vectorizer
- `requirements.txt` – runtime dependencies
- `.gitignore` – ignores venv/IDE/caches

---

## 🚀 Features
- Preprocesses text (lowercasing, tokenization, stopword removal, stemming)
- TF-IDF vectorization
- Trained ML model (Multinomial Naive Bayes)
- Interactive **Streamlit UI** for easy testing
- Deployed on **Streamlit Community Cloud**

---

## 🛠️ Tech Stack
- **Python 3**
- **NLTK** – tokenization, stopwords, stemming
- **Scikit-learn** – ML model + TF-IDF vectorizer
- **Streamlit** – web app deployment

---

## 💻 Run Locally
```bash
# Clone this repository
git clone https://github.com/your-username/sms-spam-classifier.git
cd sms-spam-classifier

# Install dependencies
pip install -r requirements.txt

# Download NLTK resources
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# Run the Streamlit app
streamlit run app.py
