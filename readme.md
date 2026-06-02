# Student Performance Predictor API

A beginner-friendly Machine Learning web application built using Flask and Scikit-learn.

This project predicts whether a student is likely to **Pass** or **Fail** based on:

* Study Hours
* Attendance
* Sleep Hours
* Previous Scores

The application includes:

* Machine Learning model
* Flask backend API
* Frontend UI
* JSON-based API communication

---

# Tech Stack

## Backend

* Python
* Flask

## Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib

## Frontend

* HTML
* CSS
* JavaScript

---

# Project Structure

```text
student-ml-api/
│
├── app.py
├── train.py
├── students.csv
├── student_model.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# Features

* Logistic Regression ML model
* Student pass/fail prediction
* REST API using Flask
* Frontend integration
* Probability-based prediction
* JSON request/response handling

---

# How It Works

```text
Frontend
   ↓
Flask API
   ↓
Machine Learning Model
   ↓
Prediction Response
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
cd student-ml-api
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Train Machine Learning Model

Run:

```bash
python train.py
```

This creates:

```text
student_model.pkl
```

---

## 5. Start Flask Application

```bash
python app.py
```

Application runs at:

```text
http://127.0.0.1:5000
```

---

# API Endpoint

## POST /predict

### Request Body

```json
{
  "study_hours": 7,
  "attendance": 90,
  "sleep_hours": 7,
  "previous_score": 80
}
```

### Response

```json
{
  "prediction": "Pass",
  "pass_probability": 0.97
}
```

---

# Machine Learning Model

The project uses:

```python
LogisticRegression()
```

from Scikit-learn.

The model predicts:

* Pass
* Fail

based on:

* Study Hours
* Attendance
* Sleep Hours
* Previous Score

---
