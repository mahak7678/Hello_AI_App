import streamlit as st
import numpy as np
from model import train

st.title("Hello World App")
st.subheader("This is a simple regression model")

model=train()

st.sidebar.header("Input parameters:")
input_values=st.sidebar.slider("Select a value",1,10,1)

input_array=np.array([[input_values]])
prediction=model.predict(input_array)
st.write(f"The input value is:{input_values}")
st.write(f"The predicted value is:{prediction[0]:.2f}")