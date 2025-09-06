# session_3_flask_intro

## Overview
This project is a Flask web application that utilizes a machine learning model to make predictions based on user input. The model is trained using data from a CSV file and is serialized for use in the application.

## Project Structure
```
session_3_flask_intro
├── app.py                # Main application file for the Flask web app
├── requirements.txt      # Lists dependencies required for the project
├── train_ml.ipynb       # Jupyter Notebook for training the machine learning model
├── classifier.pkl        # Serialized version of the trained machine learning model
├── train_flask.csv       # Training data used for the machine learning model
└── README.md             # Documentation for the project
```

## Setup Instructions
1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd session_3_flask_intro
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask application:
   ```
   python app.py
   ```
2. Access the application in your web browser at `http://127.0.0.1:5000`.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.