🩺 Diabetes Prediction System

A machine learning-based web application that predicts the likelihood of diabetes using patient health information. The system uses a trained machine learning model and a Flask web application to provide predictions through a simple and user-friendly interface.

📌 Project Overview

Diabetes is a common health condition that affects millions of people worldwide. Early prediction can help individuals become more aware of their health and encourage them to seek professional medical advice.

This project demonstrates how machine learning can be integrated with a web application to predict diabetes based on selected patient details.

The application allows users to enter health information such as age, blood pressure, blood sugar level, and BMI. The trained machine learning model processes the input and provides a prediction.

🎯 Objectives
Develop a machine learning model for diabetes prediction.
Create a user-friendly web interface using Flask.
Accept patient health information through a web form.
Integrate the trained model into a Flask application.
Display prediction results through a web interface.
Demonstrate the practical application of machine learning.
🛠️ Technologies Used
Technology	Purpose
Python	Programming language
Flask	Web application framework
Scikit-learn	Machine learning
NumPy	Numerical computations
HTML	Frontend structure
CSS	Webpage styling
Pickle	Saving and loading the trained model
Git & GitHub	Version control
📂 Project Structure
diabetes-prediction-system/
│
├── app.py
├── hospital.csv
├── diabetes_model.pkl
│
├── models/
│   └── diabetes_predict.py
│
├── templates/
│   └── index.html
│
├── README.md
└── requirements.txt

Note: The project structure above is based on the files visible in your VS Code screenshots. Add or remove files if your actual project differs.

⚙️ Features
Simple and user-friendly interface.
Patient health information input.
Machine learning-based prediction.
Flask backend integration.
Trained model saved using Pickle.
Fast prediction through a web application.
🧠 Machine Learning Model

The system uses a trained machine learning model to predict diabetes.

Input Features

The application accepts the following features:

Age
Blood Pressure
Blood Sugar
BMI

These values are passed to the trained model in the same order used during training.

Prediction Process
User Input
    ↓
Flask Web Application
    ↓
Input Processing
    ↓
Trained Machine Learning Model
    ↓
Prediction
    ↓
Display Result
