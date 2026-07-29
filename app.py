import streamlit as st
if "music_on" not in st.session_state:
    st.session_state.music_on = False
from database import connect
import vision_utils

st.set_page_config(
    page_title="AI VisionTale",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)
vision_utils.play_background_music()

connect()
st.switch_page("pages/1_Home.py")

