import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('best_model.joblib')

# Function to predict crop based on environmental conditions
def predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    """
    Predicts the best crop based on environmental conditions.
    
    Args:
        nitrogen (float): Amount of nitrogen
        phosphorus (float): Amount of phosphorus
        potassium (float): Amount of potassium
        temperature (float): Temperature in degrees Celsius
        humidity (float): Humidity in percentage
        ph (float): pH level of the soil
        rainfall (float): Amount of rainfall in millimeters
    
    Returns:
        str: Predicted crop
    """
    data = pd.DataFrame({
        'Nitrogen': [nitrogen],
        'phosphorus': [phosphorus],
        'potassium': [potassium],
        'temperature': [temperature],
        'humidity': [humidity],
        'ph': [ph],
        'rainfall': [rainfall]
    })
    prediction = model.predict(data)[0]
    return prediction

# Streamlit app
def main():
    # Set page title and subtitle
    st.set_page_config(page_title="Crop Recommendation", page_icon="🌾", layout="wide")
    st.title("🌱 Crop Recommendation System 🌱")
    st.write("This app suggests the best crop to grow based on the given environmental conditions.")

    # Create input fields
    col1, col2 = st.columns(2)
    with col1:
        nitrogen = st.number_input("Nitrogen Level", min_value=0.0, step=0.1, format="%.1f")
        phosphorus = st.number_input("Phosphorus Level", min_value=0.0, step=0.1, format="%.1f")
        potassium = st.number_input("Potassium Level", min_value=0.0, step=0.1, format="%.1f")
    with col2:
        temperature = st.number_input("Temperature (°C)", min_value=-20.0, max_value=50.0, step=0.1, format="%.1f")
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=1.0, format="%d")
        ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, step=0.1, format="%.1f")
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1, format="%.1f")

    # Add predict button
    if st.button("Predict Best Crop"):
        try:
            predicted_crop = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
            st.success(f"The best crop to grow is: {predicted_crop}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Run the app
if __name__ == "__main__":
    main()
