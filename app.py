import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Ensure required NLTK data is available on first run (e.g., Streamlit Cloud)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

ps=PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf=pickle.load(open('vectorizer.pkl', 'rb'))
model=pickle.load(open('modle.pkl', 'rb'))

st.title(' SMS/Email Spam Classification')

input_sms = st.text_area('Enter your message')

if st.button('Classify'):


    #1.preprocess
    transformed_sms=transform_text(input_sms)

    #2.vectorize
    vector_input=tfidf.transform([transformed_sms])

    #3.predict
    result=model.predict(vector_input)

    #4.display
    if result == 1:
        st.header('Your Message is a spam message')
    else:
        st.header('Your Message is not a spam message')




