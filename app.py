from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

app = Flask("Humpty - Your Doctor")

# Load training data
df = pd.read_csv("Training.csv")

# Create disease-to-index mapping
disease_mapping = {disease: i for i, disease in enumerate(df['prognosis'].unique())}
df.replace({'prognosis': disease_mapping}, inplace=True)

# Reverse mapping (index to disease)
reverse_mapping = {v: k for k, v in disease_mapping.items()}

X = df.iloc[:, :-1]
y = df['prognosis']

# Load testing data
tr = pd.read_csv("Testing.csv")
tr.replace({'prognosis': disease_mapping}, inplace=True)
X_test = tr.iloc[:, :-1]
y_test = tr['prognosis']

# Train models
dt_model = tree.DecisionTreeClassifier().fit(X, y)
rf_model = RandomForestClassifier().fit(X, y)
nb_model = GaussianNB().fit(X, y)

# List of symptoms
symptoms = list(X.columns)

# Precautions and specialists dictionary
precautions = {
    "Fungal infection": {
        "precautions": ["Keep the affected area clean and dry.", "Use antifungal creams.", "Avoid sharing personal items."],
        "specialist": "Dermatologist"
    },
    "Diabetes": {
        "precautions": ["Maintain a balanced diet.", "Exercise regularly.", "Monitor blood sugar levels."],
        "specialist": "Endocrinologist"
    },
    "Malaria": {
        "precautions": ["Use mosquito nets.", "Wear protective clothing.", "Take antimalarial medications if prescribed."],
        "specialist": "Infectious Disease Specialist"
    },
    "Dengue": {
        "precautions": ["Avoid mosquito bites.", "Stay hydrated.", "Seek medical attention if symptoms worsen."],
        "specialist": "General Physician"
    },
    "Common Cold": {
        "precautions": ["Drink warm fluids.", "Rest well.", "Avoid cold weather."],
        "specialist": "General Physician"
    },
    "Bronchial Asthma": {
        "precautions": ["Avoid allergens.", "Use prescribed inhalers.", "Maintain a clean environment."],
        "specialist": "Pulmonologist"
    },
    "Typhoid": {
        "precautions": ["Drink clean water.", "Maintain hygiene.", "Eat well-cooked food."],
        "specialist": "General Physician"
    },
    "GERD": {
        "precautions": ["Eat smaller meals.", "Avoid spicy and acidic foods.", "Don't lie down immediately after eating."],
        "specialist": "Gastroenterologist"
    }
}

@app.route('/')
def home():
    return render_template("index.html", symptoms=symptoms)

@app.route('/predict', methods=['POST'])
def predict():
    selected_symptoms = request.form.getlist('symptoms')
    input_vector = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]

    dt_index = int(dt_model.predict([input_vector])[0])
    rf_index = int(rf_model.predict([input_vector])[0])
    nb_index = int(nb_model.predict([input_vector])[0])

    print(f"Predicted indices - DT: {dt_index}, RF: {rf_index}, NB: {nb_index}")  # Debugging
    print(f"Reverse Mapping Keys: {reverse_mapping.keys()}")  # Debugging

    # Convert indices back to disease names
    dt_prediction = reverse_mapping.get(dt_index, "Unknown Disease").strip()
    rf_prediction = reverse_mapping.get(rf_index, "Unknown Disease").strip()
    nb_prediction = reverse_mapping.get(nb_index, "Unknown Disease").strip()

    print(f"Predicted Diseases - DT: {dt_prediction}, RF: {rf_prediction}, NB: {nb_prediction}")  # Debugging

    # Get precautions and specialist for the predicted disease
    dt_precaution = precautions.get(dt_prediction, {"precautions": ["No specific precautions found."], "specialist": "Consult a doctor"})
    
    return render_template("index.html", symptoms=symptoms, 
                           dt_prediction=dt_prediction, 
                           rf_prediction=rf_prediction, 
                           nb_prediction=nb_prediction,
                           precautions=dt_precaution["precautions"],
                           specialist=dt_precaution["specialist"],
                           warning="⚠ This is a prediction. Please consult a doctor for professional medical advice.")

if __name__ == '__main__':
    app.run(debug=True)
