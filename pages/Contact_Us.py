import streamlit as st
from send_email import send_email

st.title("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input(label="Your email address",
                               placeholder="example@gmail.com")
    message = st.text_area(label="Your message")
    button = st.form_submit_button("Submit")

    if button:
        send_email(user_email, message)
        st.info("Your email was sent successfully!")
