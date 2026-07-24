import base64
import streamlit as st

def get_base64(file_path):
    with open(file_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return encoded



def play_background_music():

    music_file = "assets/audio/background.mp3"

    try:
        with open(music_file, "rb") as audio:
            data = audio.read()

        b64 = base64.b64encode(data).decode()

        st.markdown(
            f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True
        )

    except FileNotFoundError:
        st.error(f"Music file not found: {music_file}")