import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1 :
    st.image("Images/me.jpg", width=400)

with col2:
    st.title("Aaryan Shrestha")
    introduction = """
        Hi, I am Aaryan! I am a student currently pursuing a Bachelor's in Information Technology (BIT). I have a keen interest in coding and enjoy expanding my knowledge in this field. In my free time, I like to explore different programming languages and improve my skills, especially in frontend development and Python. Though I am still learning, I am passionate about coding and eager to develop my expertise further. My goal is to keep improving and gain hands-on experience in the tech world.
    """
    st.info(introduction)

description = """
        Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(description)


# Project Section
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# Converting the data.csv file into a well-structured table using pandas
df  = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")




