import pickle
import streamlit as st


with open('Gold Price/gold_price_model_randomForest.pkl', 'rb') as file:
  model = pickle.load(file)

st.title("Gold Price Prediction")

spx = st.number_input("Enter the S&P 500 Index")
uso = st.number_input("Enter the USO Index")
slv = st.number_input("Enter the Silver Index")
usd = st.number_input("Enter the USD Index")

data = [[spx, uso, slv, usd]]

if st.start_button("Predict"):
  prediction = model.predict(data)
  st.write(f"The predicted gold price is: {prediction[0]}")
