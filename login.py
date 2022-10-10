import streamlit as st 
st.title("Admin Login")
with st.form("my_form", clear_on_submit = True):
	username = st.text_input("Enter username:", placeholder="Username") 
	password = st.text_input("Enter password:", type="password",placeholder="Password")
	submitted = st.form_submit_button() 
	if submitted:
		if username != "Kaushik": 
			st.error("Enter proper username.")
		if password != "CMPN": 
			st.error("Enter proper password.")
		if username == "Kaushik" and password == "CMPN": 
			st.success("Successfully logged in.")
