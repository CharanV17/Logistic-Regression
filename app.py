from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("student_model.pkl")

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    features = [[
        data["study_hours"],
        data["attendance"],
        data["sleep_hours"],
        data["previous_score"]
    ]]

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0][1]

    result = "Pass" if prediction == 1 else "Fail"

    return jsonify({
        "prediction": result,
        "pass_probability": round(float(probability), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)