import vision_utils
import streamlit as st


st.set_page_config(
    page_title="AI VisionTale",
    page_icon="📖",
    layout="wide"
)



st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

section[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)
bg = vision_utils.get_base64("assets/images/background.png")


page_bg = f"""
<style>

#MainMenu {{
visibility:hidden;
}}

header {{
visibility:hidden;
}}

footer {{
visibility:hidden;
}}

.stApp {{

background-image: url("data:image/png;base64,{bg}");

background-size: cover;

background-position: center;

background-repeat: no-repeat;

background-attachment: fixed;

}}


</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)
with open("style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )


    # Glass Card - Title
st.markdown("""
<div class="glass-card">

<div class="title">
AI VisionTale
</div>

<div class="subtitle">
✨ Every Picture Opens a New Fairytale! ✨
</div>

</div>
""", unsafe_allow_html=True)

st.write("")

# Center Button
col1, col2, col3 = st.columns([2.2,2,2])

with col2:
    if st.button("📖 Open the Magic Book", use_container_width=True):
        st.switch_page("pages/2_Login.py")

   