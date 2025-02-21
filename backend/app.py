from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import joblib

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Load the model and vectorizer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "spam_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@app.route("/")
def home():
    return "Spam Classification API is running!"

# Explicitly handle OPTIONS preflight requests
@app.route("/classify", methods=["OPTIONS"])
def options():
    response = jsonify({"message": "CORS preflight request successful"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return response

@app.route("/classify", methods=["POST"])
def classify():
    try:
        data = request.get_json()

        if not data or "email_text" not in data:
            return jsonify({"error": "Invalid request, 'email_text' missing"}), 400

        # Transform input text
        email_text = data["email_text"]
        email_vectorized = vectorizer.transform([email_text])

        # Make prediction
        prediction = model.predict(email_vectorized)[0]
        result = "Spam" if prediction == 1 else "Not Spam"

        # Create response object
        response = jsonify({"prediction": result})

        # Add CORS headers manually
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")

        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
