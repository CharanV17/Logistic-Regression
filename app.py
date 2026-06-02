from flask import Flask, request, jsonify
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("student_model.pkl")

@app.route("/")
def home():
    return jsonify({
        "message": "Student ML Prediction API Running"
    })

@app.route("/predict", methods=["POST"])
def predict():

    # Get JSON data
    data = request.get_json()

    # Extract features
    features = [[
        data["study_hours"],
        data["attendance"],
        data["sleep_hours"],
        data["previous_score"]
    ]]

    # Predict
    prediction = model.predict(features)[0]

    # Probability
    probability = model.predict_proba(features)[0][1]

    return jsonify({
        "prediction": int(prediction),
        "pass_probability": round(float(probability), 2)
    })

# Run app
if __name__ == "__main__":
    app.run(debug=True)