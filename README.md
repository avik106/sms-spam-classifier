# 📩 SMS Spam Classifier using (TF-IDF + Multinomial Naive Bayes)

A machine learning project to classify SMS messages as **Spam** or **Not Spam** using natural language processing techniques and a Multinomial Naive Bayes classifier.

---

## 🚀 Demo

Try the live demo: [https://sms-spam-classifier-ndagoawhslueoxukavhp6n.streamlit.app/](#)  


---

## 🔍 Overview

This is a **binary text classification** project that:
- Preprocesses raw SMS text messages.
- Converts text into TF-IDF feature vectors.
- Trains a **Multinomial Naive Bayes** model.
- Predicts whether a new message is spam or not.

---

## 📂 Dataset

- **Source:** [SMS Spam Collection Dataset (UCI)]
- Contains 5,574 SMS messages labeled as **spam** or **not Spam**.
- Two columns:
  - `label`: `spam` or `not Spam`
  - `message`: the SMS text content

---

## 🧠 Model

- **Vectorization**: TF-IDF (`TfidfVectorizer`)
- **Classifier**: Multinomial Naive Bayes (`MultinomialNB`)
- **Accuracy**: ~97% on test set
- **Precision**: 100 on test set
---

## ⚙️ How It Works

1. **Text Preprocessing**
   - Lowercasing
   - Removing punctuation/special characters
   - Removing stopwords
   - stemming or lemmatization

2. **Feature Extraction**
   - Convert preprocessed text into numeric vectors using **TF-IDF**

3. **Model Training**
   - Train a **Multinomial Naive Bayes** classifier on TF-IDF vectors

4. **Prediction**
   - For a new SMS, the model returns `spam` or `not Spam` with probability

---
# Author - Avik Sarkar
