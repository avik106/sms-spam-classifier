import streamlit as st 
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
import string
tfidf=pickle.load(open('vectorizer.pkl','rb'))
mnb=pickle.load(open('model.pkl','rb'))
st.title("SMS Spam Classifier")
def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    l=[]
    for i in text:
        if i.isalnum():
            l.append(i)
            
    text=l[:]
    l.clear()
   
    for i in text:
       if i not in stopwords.words('english') and i not in string.punctuation:
              l.append(i)
    text=l[:]
    l.clear()
    
    for i in text:
        l.append(ps.stem(i))
        
    return " ".join(l)

input_message=st.text_area("Enter the message")
if st.button('Predict'):
    transformed_input=transform_text(input_message)
    vector_input=tfidf.transform([transformed_input])
    result=mnb.predict(vector_input)[0]
    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")