from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('classifier.pkl')

@app.route('/')
def home():
    return "Welcome to the Loan Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Convert the input data into a DataFrame
    input_data = pd.DataFrame([data])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return the prediction as a JSON response
    return jsonify({'Loan_Status': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)