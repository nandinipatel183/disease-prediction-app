# 🩺 Dr. Silky – AI-Powered Disease Prediction System

Dr. Silky is an intelligent healthcare assistant that predicts possible diseases based on user-selected symptoms using Machine Learning algorithms. The system provides disease predictions, precautionary measures, and specialist recommendations to help users make informed healthcare decisions.

> ⚠️ This application is intended for educational and informational purposes only and should not replace professional medical advice.

---

## 🚀 Features

### 🤖 Disease Prediction

Predicts diseases using multiple Machine Learning algorithms:

* Decision Tree Classifier
* Random Forest Classifier
* Gaussian Naive Bayes

### 🩺 Symptom-Based Diagnosis

Users can select symptoms from a predefined list and receive disease predictions instantly.

### 📋 Health Recommendations

For predicted diseases, the system provides:

* Precautionary measures
* Recommended specialist doctors
* Basic healthcare guidance

### 👨‍⚕️ Specialist Suggestions

Suggests appropriate medical specialists such as:

* Dermatologists
* Endocrinologists
* Pulmonologists
* Gastroenterologists
* General Physicians
* Infectious Disease Specialists

---

## 🏗️ System Architecture

```text
User Input Symptoms
          │
          ▼
   Feature Vector Creation
          │
          ▼
 Machine Learning Models
 ├── Decision Tree
 ├── Random Forest
 └── Naive Bayes
          │
          ▼
 Disease Prediction
          │
          ▼
 Precautions & Specialist Recommendations
```

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Backend

* Flask

### Machine Learning

* Scikit-learn
* Decision Tree Classifier
* Random Forest Classifier
* Gaussian Naive Bayes

### Data Processing

* Pandas
* NumPy

### Deployment

* Render
* Gunicorn

---

## 📂 Project Structure

```text
Disease-Prediction-App/
│
├── app.py
├── Training.csv
├── Testing.csv
├── requirements.txt
├── Procfile
│
├── templates/
│   └── index.html
│
├── static/
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/nandinipatel183/disease-prediction-app.git
cd disease-prediction-app
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Application will start on:

```text
http://127.0.0.1:5000
```

---

## 📊 Machine Learning Models

The application trains and compares predictions from:

### Decision Tree

* Rule-based disease classification
* Fast prediction

### Random Forest

* Ensemble learning approach
* Improved prediction stability

### Gaussian Naive Bayes

* Probabilistic classification model
* Efficient for symptom-based predictions

---

## 🧪 Dataset

The application uses:

* Training.csv
* Testing.csv

Datasets contain:

* Symptoms as features
* Disease prognosis as target labels

---

## 📋 Supported Features

✅ Disease Prediction

✅ Precaution Suggestions

✅ Specialist Recommendations

✅ Multiple ML Models

✅ User-Friendly Interface

✅ Real-Time Predictions

---

## 🔮 Future Enhancements

* AI Chatbot Integration
* Voice-Based Symptom Input
* Medical Report Analysis
* Doctor Appointment Recommendations
* Medicine Recommendations
* Health Risk Assessment
* Disease Prediction Confidence Scores
* Mobile Application Version

---

## 👩‍💻 Developer

### Nandini Patel

M.Tech (Information Technology)

International Institute of Professional Studies (IIPS), DAVV

GitHub: https://github.com/nandinipatel183

---

## 📜 License

This project is licensed under the MIT License.

---

## ⚠️ Disclaimer

This system provides machine-learning-based predictions and recommendations. Results may not always be accurate. Always consult a qualified healthcare professional for diagnosis and treatment.
