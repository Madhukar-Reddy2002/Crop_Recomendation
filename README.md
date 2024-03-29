# Crop Recommendation System
This project provides a user-friendly web application built with Streamlit to recommend crops based on environmental conditions.

## Functionality:
Users can input various environmental factors like nitrogen, phosphorus, potassium levels, temperature, humidity, pH, and rainfall.
The pre-trained machine learning model analyzes these inputs and predicts the most suitable crop for those conditions.
The app displays the predicted crop as output.
Prerequisites:
Python (version 3.6 or later)
Libraries:
streamlit
pandas
joblib
Note: This project assumes you have a pre-trained machine learning model saved as best_model.joblib that can be loaded using joblib. You'll need to train and save your own model for this to function completely.

## Running the Project:
Install required libraries: pip install streamlit pandas joblib
Ensure you have best_model.joblib in the same directory as your main Python script (e.g., main.py).
Run the script: python main.py
This will launch the Streamlit app in your web browser, typically at http://localhost:8501.

## Usage:
Enter values for the environmental factors in the designated input fields.
Click the "Predict Best Crop" button.
The app will analyze the data and display the recommended crop in a success message.