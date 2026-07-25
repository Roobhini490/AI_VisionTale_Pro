import streamlit as st
import os
from vision_utils import get_base64
import vision_utils
from vision_utils import play_background_music

if "music_on" not in st.session_state:
    st.session_state.music_on = True   # Music ON by default

if st.session_state.music_on:
    play_background_music()


st.set_page_config(
    page_title="Story History",
    page_icon="📚",
    layout="wide"
)
bg = get_base64("assets/images/background.png")

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
st.markdown(f"""
<style>

#MainMenu{{visibility:hidden;}}
header{{visibility:hidden;}}
footer{{visibility:hidden;}}

.stApp{{
background-image:url("data:image/png;base64,{bg}");
background-size:cover;
background-position:center;
background-repeat:no-repeat;
background-attachment:fixed;
}}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style="
text-align:center;
font-family:'Chewy', cursive;
font-size:60px;
color:#FF8FB1;
">
📖 Story History
</h1>
""", unsafe_allow_html=True)


os.makedirs("history", exist_ok=True)

files = sorted(
    os.listdir("history"),
    reverse=True
)

if not files:
    st.info("No stories generated yet.")

else:
    for file in files:

        if file.endswith(".txt"):

            path = os.path.join("history", file)

            with open(path, "r", encoding="utf-8") as f:
                story = f.read()

            st.markdown("---")

            title = story.split("\n")[0]
            title = title.replace("#", "").replace("*", "").strip()

            st.subheader(f"📖 {title}")

            st.text_area(
                "Story",
                story,
                height=250,
                key=file
            )

            col1, col2 = st.columns(2)

            with col1:
                st.download_button(
                    "📥 Download",
                    data=story,
                    file_name=file,
                    mime="text/plain",
                    key=f"download_{file}",
                    on_click="ignore"
                )

            with col2:
                if st.button("🗑 Delete", key=f"delete_{file}"):
                    os.remove(path)
                    st.rerun()
