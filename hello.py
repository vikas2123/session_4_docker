from flask import Flask, request, jsonify

import joblib
clf = joblib.load('classifier.pkl')

pancakes = Flask(__name__)

@pancakes.route('/hello', methods=['GET'])
def hello():
    "A simple hello world endpoint for Flask"
    return {"message": "Hello, World!"}

@pancakes.route('/', methods=['GET'])
def index():
    "A simple index endpoint for Flask"
    pancake_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pancake Created!</title>
        <style>
            body {
                background-color: #ffe5b4;
                color: #4b2e05;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }
            .card {
                background: #fff8dc;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                display: inline-block;
                padding: 40px 60px;
            }
            h1 {
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🥞 docker session -4</h1>
            <p>Your pancake is ready to enjoy.</p>
        </div>
    </body>
    </html>
    """
    return pancake_html, 201




@pancakes.route('/predict', methods=['POST'])
def predict():
    loan_req = request.get_json()

    if loan_req['Gender']=='Male' : Gender =0
    else: Gender =1

    if loan_req['Married']=='UnMarried' : Married =0
    else: Married =1

    if loan_req['Credit_History'] == "Uncleared Debts": Credit_History = 0
    else: Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']

    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        result = "Loan Rejected"
    else:
        result = "Loan Approved"

    return {"loan_approval_status": result}
 
