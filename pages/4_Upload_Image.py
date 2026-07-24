import streamlit as st
from vision_utils import get_base64
import vision_utils

if "camera_images" not in st.session_state:
    st.session_state.camera_images = []

st.set_page_config(
    page_title="Upload Image",
    page_icon="📷",
    layout="wide"
)

bg = get_base64("assets/images/background.png")

st.markdown(f"""
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

[data-testid="stSidebar"] {{
    display:none;
}}

[data-testid="collapsedControl"] {{
    display:none;
}}

.stApp {{
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
<div class="glass-card">

<h1 style="
text-align:center;
font-family:'Chewy', cursive;
font-size:60px;
color:#FF8FB1;
">

📷 Upload Your Picture

</h1>

<h3 style="
text-align:center;
color:#A8E6A3;
">

Choose a photo and let the magic begin! ✨

</h3>

</div>
""", unsafe_allow_html=True)

left, center, right = st.columns([1, 3, 1])

with center:

    st.markdown("""
    <h3 style="
    color:#6F4E7C;
    font-family:'Comic Sans MS', cursive;
    font-size:28px;
    text-align:center;
    ">
    📷 Capture a Live Photo
    </h3>
    """, unsafe_allow_html=True)

    camera_image = st.camera_input(
    "📷 Take a Photo",
    key="camera1"
)
    
    if camera_image is not None:
        left, center, right = st.columns([1, 2, 1])

        with center:

         if st.button(
            "✨ Save This Photo",
            use_container_width=True
        ):

 
          if len(st.session_state.camera_images) < 4:

            st.session_state.camera_images.append(camera_image)

            st.success("📷 Photo Added!")

          else:

            st.error("Maximum 4 camera photos allowed.")
    if len(st.session_state.camera_images) > 0:

         st.markdown("""
<h3 style="
color:#6F4E7C;
font-family:'Comic Sans MS', cursive;
text-align:center;
font-size:30px;
">
📷 Camera Photos
</h3>
""", unsafe_allow_html=True)

         cols = st.columns(4)

         for i, img in enumerate(st.session_state.camera_images):

          with cols[i]:
            st.image(
                img,
                use_container_width=True,
                caption=f"Photo {i+1}"
            )
            if st.button("🗑️", key=f"remove_camera_{i}", help="Remove Photo"):

               st.session_state.camera_images.pop(i)

               st.rerun()
   
   
    st.markdown("""
    <h2 style="
    text-align:center;
    color:#6F4E7C;
    ">
    ───── OR ─────
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3 style="
    color:#6F4E7C;
    font-family:'Comic Sans MS', cursive;
    font-size:28px;
    text-align:center;
    ">
    🖼 Upload Images
    </h3>
    """, unsafe_allow_html=True)

    uploaded_images = st.file_uploader(
    "",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True,
    label_visibility="collapsed",
    key="upload1"
)

# Count camera and uploaded photos
camera_count = len(st.session_state.camera_images)
upload_count = len(uploaded_images)

total_images = camera_count + upload_count

# Allow only 4 pictures in total
if total_images > 4:
    st.markdown("""
<div style="
background:#FFF4E5;
border:3px solid #FFB347;
border-radius:20px;
padding:18px;
text-align:center;
font-family:'Comic Sans MS', cursive;
font-size:22px;
font-weight:bold;
color:#E85D04;
">
🪄 Oops! Your magical story can use only 4 pictures.<br>
Please remove some pictures and try again! ✨
</div>
""", unsafe_allow_html=True)
    st.stop()

# Show uploaded image preview
if uploaded_images:

    st.markdown("""
<h3 style="
color:#6F4E7C;
font-family:'Comic Sans MS', cursive;
text-align:center;
font-size:30px;
">
🖼 Uploaded Photos
</h3>
""", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    columns = [col1, col2, col3, col4]

    for i, image in enumerate(uploaded_images):
        with columns[i]:
            st.image(image, use_container_width=True)

    st.write("")

left, center, right = st.columns([1.7, 2, 1])

with center:
    st.markdown("""
<h1 style="
font-family:'Comic Sans MS', cursive;
font-size:30px;
color:#6F4E7C;
">
🌍 Story Language
</h1>
""", unsafe_allow_html=True)

   

    language = st.selectbox(
    "",
    ["English", "Tamil","Hindi","German","French"],
    key="language"
)

    st.markdown("""
<h1 style="
font-family:'Comic Sans MS', cursive;
font-size:30px;
color:#6F4E7C;
">
🌍 Story Theme
</h1>
""", unsafe_allow_html=True)

    theme = st.selectbox(
    "",
    [
        "Fantasy",
        "Adventure",
        "Space",
        "Jungle",
        "Magic",
        "Underwater",
        "Animals",
        "Friendship"
    ],
    key="theme"
)


    if st.button("✨ Generate My Story ✨", use_container_width=True):

        total_images = len(st.session_state.camera_images) + len(uploaded_images)

        if total_images == 0:
            left, center, right = st.columns([0.1, 3.5, 0.5])

            with center:

             st.markdown("""
            <div style="
            background:#FFF4E5;
            border:3px solid #FFB347;
            border-radius:20px;
            padding:18px;
            text-align: center;
            font-family:'Comic Sans MS', cursive;
            font-size:22px;
            font-weight:bold;
            color:#E85D04;
            ">
            🪄 Please add at least one magical picture before creating your story! ✨
            </div>
            """, unsafe_allow_html=True)

        else:

           # Store all selected images
         all_images = []

# Camera images
         for img in st.session_state.camera_images:
           all_images.append(img)

# Uploaded images
         for img in uploaded_images:
           all_images.append(img)

# Save into Session State
         st.session_state.story_images = all_images

# Go to story page
         st.switch_page("pages/5_Generate_Story.py")      