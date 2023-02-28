import streamlit as st
import requests
import pandas as pd

# Set page title
st.title("Dog Pictures")

st.write("Dog Image Generator")
st.sidebar.write("## Select Your Favorite Species: :dog:")

#read csv file and create submit button
form = st.sidebar.form(key='dog_selection_form')
selected_dog = form.selectbox(
    'Select Your Option',
    pd.read_csv("dog_list.csv")["Breed names"].tolist())
submit = form.form_submit_button('submit')

#get url and display image
if submit:
    url = f"https://dog.ceo/api/breed/{selected_dog}/images/random"
    response = requests.get(url)
    image_url = response.json()["message"]
    st.image(image_url)
