# Wildfire Prediction using Ridge Regression

This is a Flask web application that predicts wildfire probability based on several environmental factors using a Ridge Regression model. The app allows users to input environmental data and provides predictions based on a pre-trained Ridge Regression model.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Model and Preprocessing](#model-and-preprocessing)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Connect with Me](#connect-with-me)

## Overview

This application is designed to predict wildfire occurrences based on inputs like temperature, relative humidity (RH), wind speed (Ws), rain, and other environmental variables. It uses a pre-trained Ridge Regression model and a standard scaler to preprocess the input data before making predictions.

The main features of this application are:
- **Input:** Users can input environmental factors via a web form.
- **Prediction:** The application will return a prediction result, which can be interpreted as the likelihood of wildfire occurrence.

## Technologies Used

- **Flask**: Web framework for creating the backend API and web pages.
- **Scikit-Learn**: Machine learning library used for the Ridge Regression model and data preprocessing.
- **Pickle**: Used for loading the pre-trained machine learning model and scaler.
- **HTML**: For rendering web pages via Flask's `render_template` method.
- **Python**: Core language used to build the application.

## Model and Preprocessing

The Ridge Regression model (`ridge.pkl`) was trained on environmental data to predict wildfire probabilities. Data preprocessing was done using a `StandardScaler` (`scaler.pkl`) to ensure all input features are normalized before being fed into the model.

The environmental factors considered in the prediction:
- Temperature
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rainfall
- FFMC (Fine Fuel Moisture Code)
- DMC (Duff Moisture Code)
- ISI (Initial Spread Index)
- Classes (Fire risk classification)
- Region (Geographical region)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wildfire-prediction.git
2. Navigate to the project directory:
   ```bash
   cd wildfire-prediction
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Add the pre-trained models (ridge.pkl, scaler.pkl) to the models directory.

## Usage

1. Run the Flask application:
   ```bash
   python app.py
2. Open your browser and navigate to:
   ```bash
   http://127.0.0.1:5000/
3. Enter the required environmental data on the homepage form and get the prediction results.

## Folder Structure
    wildfire-prediction/
    │
    ├── app.py                   # Main application file
    ├── models/
    │   ├── ridge.pkl            # Pre-trained Ridge Regression model
    │   └── scaler.pkl           # Pre-trained Standard Scaler
    ├── templates/
    │   ├── index.html           # Main input form page
    │   └── home.html            # Result page
    ├── static/                  # Static files (CSS, images, etc.)
    ├── requirements.txt         # Python dependencies
    └── README.md                # Project documentation


## Connect with Me

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/shivam-u/), [Twitter](https://x.com/Shivam_Twtss) or check out my other projects on [GitHub](https://github.com/Shivam-Upa).

<!--
## Screenshots

  ### Homepage
  ### Prediction Result
-->
  
