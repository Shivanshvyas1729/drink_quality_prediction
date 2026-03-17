from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
from mlproject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

# ==============================
# Home Page
# ==============================
@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")


# ==============================
# Train Route
# ==============================
@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return redirect(url_for('homePage'))


# ==============================
# Prediction Route
# ==============================
@app.route('/predict', methods=['POST', 'GET'])
def predict():

    if request.method == "POST":
        try:
            # Get form values
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            # Create DataFrame with SAME column names used in training
            columns = [
                'fixed acidity',
                'volatile acidity',
                'citric acid',
                'residual sugar',
                'chlorides',
                'free sulfur dioxide',
                'total sulfur dioxide',
                'density',
                'pH',
                'sulphates',
                'alcohol'
            ]

            data = pd.DataFrame([[ 
                fixed_acidity, volatile_acidity, citric_acid,
                residual_sugar, chlorides, free_sulfur_dioxide,
                total_sulfur_dioxide, density, pH,
                sulphates, alcohol
            ]], columns=columns)

            # Load prediction pipeline
            obj = PredictionPipeline()
            prediction = obj.predict(data)

            # Extract value from array
            final_result = prediction[0]

            return render_template("result.html", prediction=str(final_result))

        except Exception as e:
            print("Error:", e)
            return "Something went wrong"

    return render_template("index.html")


# ==============================
# Run App
# ==============================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)