# python -m venv venv
# venv\Scripts\activate


# streamlit_app.py
# streamlit run streamlit_app.py

import streamlit as st
import requests
import os

st.set_page_config(page_title="Iris Predictor", page_icon="🌸")
st.title("🌸 Iris Species Predictor")

st.markdown("Enter the features below:")

# Get API URL from environment variable or default to localhost
API_URL = os.getenv("FLASK_API_URL", "http://localhost:5000/predict")

# Inputs
sl = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sw = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
pl = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
pw = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

if st.button("Predict"):
    features = [sl, sw, pl, pw]
    try:
        response = requests.post(API_URL, json={"feature_array": features})
        if response.status_code == 200:
            result = response.json()
            class_map = ["Setosa", "Versicolor", "Virginica"]
            predicted_class = class_map[result["prediction"][0]]
            st.success(f"🌿 Predicted Iris Species: **{predicted_class}**")
        else:
            st.error(f"Server returned error: {response.text}")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")


# import streamlit as st
# import requests

# st.set_page_config(page_title="Iris Predictor", page_icon="🌸")
# st.title("🌸 Iris Species Predictor")

# st.markdown("Enter the features below:")

# # Inputs
# sl = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
# sw = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
# pl = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
# pw = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

# if st.button("Predict"):
#     features = [sl, sw, pl, pw]
#     try:
#         response = requests.post("http://localhost:5000/predict", json={"feature_array": features})
#         if response.status_code == 200:
#             result = response.json()
#             class_map = ["Setosa", "Versicolor", "Virginica"]
#             predicted_class = class_map[result["prediction"][0]]
#             st.success(f"🌿 Predicted Iris Species: **{predicted_class}**")
#         else:
#             st.error(f"Server returned error: {response.text}")
#     except Exception as e:
#         st.error(f"Error connecting to API: {e}")

