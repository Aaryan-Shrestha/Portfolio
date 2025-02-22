import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1 :
    st.image("Images/me.jpg", width=400)

with col2:
    st.title("Aaryan Shrestha")
    content = """
        Hi, I am Aaryan! I am a student currently pursuing a Bachelor's in Information Technology (BIT). I have a keen interest in coding and enjoy expanding my knowledge in this field. In my free time, I like to explore different programming languages and improve my skills, especially in frontend development and Python. Though I am still learning, I am passionate about coding and eager to develop my expertise further. My goal is to keep improving and gain hands-on experience in the tech world.
    """
    st.info(content)
