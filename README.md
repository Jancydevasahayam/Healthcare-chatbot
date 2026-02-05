#  Offline Healthcare Chatbot using Machine Learning

An **AI-powered Healthcare Chatbot** that predicts diseases based on user-entered symptoms.  
The system works **completely offline**, uses **machine learning**, and provides a **simple, catchy user interface**.

##  Project Overview

Healthcare diagnosis is often time-consuming and dependent on expert availability.  
This project aims to assist users by providing **instant disease predictions** based on symptoms using a trained ML model.

### Key Features
-  Works **100% offline**
-  Machine Learning–based disease prediction
-  Simple and user-friendly interface
-  Fast response time
-  Easy to extend with more datasets or UI features

## Technologies Used

- **Python 3**
- **Pandas** – data processing
- **Scikit-learn** – ML model
- **TF-IDF Vectorizer** – text feature extraction
- **Naive Bayes Classifier**
- **Joblib** – model saving/loading
- **Tkinter / Streamlit** – UI (offline)

## Project Structure

healthcare_chatbot/
│
├── dataset.csv
├── preprocess.py
├── processed_dataset.csv
├── train_model.py
├── disease_model.pkl
├── vectorizer.pkl
├── chatbot_app.py
├── requirements.txt
└── README.md
