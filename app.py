import streamlit as st
import sklearn
import helper
import pickle
import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')

model = pickle.load(open('models/model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))

st.title('Sentiment Analysis App using ML')
st.text('Hello, world!')
text = st.text_input('Enter your review here')

token = helper.preprocessing_step(text)

vector = vectorizer.transform([token])

prediction = model.predict(vector)

prediction = ['Positive' if prediction[0] == 1 else 'Negative']

state = st.button('Predict')
if state:
    st.markdown((
    f"The review you have entered : <u><b>{text}</b></u>  \n"
    f"Sentiment : <u><b>{prediction[0]} review</b></u>"
), unsafe_allow_html=True)
  