import streamlit as st 
import joblib 

model_nb = joblib.load('Pass-Fail')

st.title("PASS FAIL CLASSIFIER")
ip = st.text_input("Enter The Marks:")

op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])  
  
  

   
 
