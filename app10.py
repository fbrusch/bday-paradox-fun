import streamlit as st

st.title("Birthday collision calculator!!")


st.write("Hi user! Please tell me how many people do you want in the class")

number = st.number_input("n")

from random import randint

if st.button("press me"):
    c = [randint(1,365) for _ in range(int(number))]

    st.write(c)
