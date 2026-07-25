import streamlit as st
from vision_utils import get_base64
from gemini_service import generate_story
from PIL import Image
import time
import streamlit.components.v1 as components
import json
from gtts import gTTS
import os
from datetime import datetime
from vision_utils import play_background_music

play_background_music()


images = st.session_state.get("story_images", [])

st.set_page_config(
    page_title="Generating Story",
    page_icon="📖",
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

with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<h1 style="
text-align:center;
font-family:'Chewy', cursive;
font-size:60px;
color:#FF8FB1;
">
📖 Creating Your Magical Story...
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style="
text-align:center;
font-family:'Comic Sans MS', cursive;
color:#C9A0DC;
font-size:30px;            
">
✨ Please wait while AI creates your adventure... ✨
</h3>
""", unsafe_allow_html=True)


st.markdown("""
<h3 style="
color:#C9A0DC;
font-family:'Comic Sans MS', cursive;
text-align:center;
font-size:30px;
">
Images Received for Story Generation 
</h3>
""", unsafe_allow_html=True)

cols = st.columns(4)

for i, img in enumerate(images):

    with cols[i]:
        st.image(img, use_container_width=True)

st.write("")

with st.spinner("🪄 AI is creating your magical story..."):

    if "story" not in st.session_state:

        pil_images = []

        for img in images:
            pil_images.append(Image.open(img))

        story = generate_story(pil_images)

        st.session_state["story"] = story

        tts = gTTS(text=story, lang="en")

        audio_path = "assets/audio/story.mp3"

        tts.save(audio_path)

        st.session_state["audio_path"] = audio_path

        os.makedirs("history", exist_ok=True)

        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"

        with open(f"history/{filename}", "w", encoding="utf-8") as f:
            f.write(story)
            

story = st.session_state["story"]
audio_path = st.session_state["audio_path"]


with st.spinner("🪄 Sprinkling fairy dust..."):
    import time
    time.sleep(3)

components.html(f"""
<!DOCTYPE html>
<html>

<head>

<style>

body{{
background:transparent;
margin:0;
}}

.book{{
background:#FFF8E7;
padding:45px;
border-radius:30px;
border:8px solid #C89B3C;
box-shadow:0px 15px 35px rgba(0,0,0,0.35);
max-width:1000px;
margin:auto;
}}

.title{{
text-align:center;
font-family:'Chewy',cursive;
font-size:52px;
color:#8B4513;
}}

.story{{
font-size:24px;
line-height:2.2;
font-family:'Comic Sans MS',cursive;
color:#4B2E2E;
text-align:justify;
white-space:pre-wrap;
}}

.end{{
text-align:center;
font-size:22px;
font-weight:bold;
color:#E45598;
}}

hr{{
border:2px dashed #D4AF37;
}}

</style>

</head>

<body>

<div class="book">

<h1 class="title">
📖 Your Magical Story 📖
</h1>

<hr>

<div id="story" class="story"></div>

<hr>

<p class="end">
✨ The End ✨
</p>

</div>

<script>

const story = {json.dumps(story)};

const words = story.split(" ");

let i = 0;

function typeWriter() {{

    if(i < words.length){{
        document.getElementById("story").innerHTML += words[i] + " ";
        i++;
        setTimeout(typeWriter,60);
    }}

}}

typeWriter();

</script>

</body>

</html>
""",
height=900,
scrolling=True)  
 
st.write("")

left, center, right = st.columns([1.5, 2, 1.5])

with center:

    st.markdown("""
   <div style="
   background:#FFF8E7;
   border:5px solid #C89B3C;
   border-radius:20px;
   padding:15px;
   margin-top:20px;
   margin-bottom:10px;
   text-align:center;
   box-shadow:0px 8px 20px rgba(0,0,0,0.2);
   ">

   <h2 style="
   margin:0;
   font-family:'Chewy', cursive;
   color:#8B4513;
   font-size:32px;
   ">
    🔊 Read Aloud
    Listen to your story with magical narration! 🎧        
    </h2>

    </div>
     """, unsafe_allow_html=True)
    st.audio(audio_path)


    st.write("")
    st.write("")
    st.download_button(
    label="📥 Download Story",
    data=story,
    file_name="My_Magical_Story.txt",
    mime="text/plain",
    use_container_width=True,
    on_click="ignore"
)
    with center:
     left, center, right = st.columns([1.7, 2, 1])

     if st.button("📚 Story History", use_container_width=True):
      st.switch_page("pages/6_Story_History.py")