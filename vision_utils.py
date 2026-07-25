
import base64
import streamlit as st


def get_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def play_background_music():

    with open("assets/audio/background.mp3", "rb") as audio:
        data = audio.read()

    b64 = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True,
    )