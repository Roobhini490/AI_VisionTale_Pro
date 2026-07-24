import streamlit as st
from vision_utils import get_base64
import time
from database import register_user
import vision_utils


st.set_page_config(
    page_title="Create Account",
    page_icon="👑",
    layout="wide"
)

bg = get_base64("assets/images/background.png")

st.markdown(f"""
  <style>

[data-testid="stSidebar"] {{
display:none;
}}

[data-testid="collapsedControl"] {{
display:none;
}}

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

background-image:url("data:image/png;base64,{bg}");

background-size:cover;

background-position:center;

background-repeat:no-repeat;

background-attachment:fixed;

}}

  </style>
""", unsafe_allow_html=True)


with open("style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )
    

    st.markdown("""
<div class="create-card">

<h1 style="
text-align:center;
font-size:52px;
color:#A8E6A3;
font-family:'Comic Sans MS',cursive;
">

✨ Create Your Magical Account

</h1>

<h3 style="
text-align:center;
color:#D8B4FE;
font-family:'Comic Sans MS',cursive;
">

Join AI VisionTale Today 🌈

</h3>
</div>
""", unsafe_allow_html=True)
    

    
left, center, right = st.columns([1,2,1])

with center:
    
    st.markdown("""
    <h3 style="
    color:#e45598;
    font-size:28px;
    font-family:'Comic Sans MS';
    ">
    👤 Username
    </h3>
  
         
    """, unsafe_allow_html=True)

    username = st.text_input(
       "",
       placeholder="Choose a username",
       label_visibility="collapsed"
)
    st.markdown("""
     <h3 style="
     color:#e45598;
     font-family:'Comic Sans MS',cursive;
     font-size:28px;
     margin-bottom:5px;
     ">
     🎂 Age
    </h3>
    """, unsafe_allow_html=True)

    age = st.selectbox(
       "",
       ["3","4","5","6","7","8","9","10","11","12"],
       label_visibility="collapsed"
)
    st.markdown("""
    <h3 style="
    color:#e45598;
    font-family:'Comic Sans MS',cursive;
    font-size:28px;
    margin-bottom:5px;
    ">
    👑 Choose Your Avatar
    </h3>
     </div>           
    """, unsafe_allow_html=True)

    avatar = st.radio(
       "",
       ["🤴 Prince", "👸 Princess"],
       horizontal=True,
       label_visibility="collapsed"
)
    st.markdown("""
    <h3 style="
    color:#e45598;
    font-family:'Comic Sans MS',cursive;
    font-size:28px;
    margin-bottom:5px;
    ">
    🔒 Password
    </h3>
    </div>            
    """, unsafe_allow_html=True)

    password = st.text_input(
      "",
      placeholder="Create a password",
      type="password",
      label_visibility="collapsed",
      key="create_password"
)
    st.markdown("""
    <h3 style="
    color:#e45598;
    font-family:'Comic Sans MS',cursive;
    font-size:28px;
    margin-bottom:5px;
    ">
    🔒 Confirm Password
    </h3>
    </div>            
    """, unsafe_allow_html=True)

    confirm_password = st.text_input(
       "",
       placeholder="Re-enter your password",
       type="password",
       label_visibility="collapsed",
       key="confirm_password"
)
   
    
    st.write("")
    left, center, right = st.columns([1,2.5,1])

with center:



 if st.button("✨ Create Account", use_container_width=True):

    if username.strip() == "":
        st.error("Please enter a username.")

    elif password.strip() == "":
        st.error("Please create a password.")

    elif password != confirm_password:
        st.error("❌ Passwords do not match.")

    else:


     success = register_user(
        username,
        age,
        avatar,
        password
    )

     if success:

        st.success("🎉 Account Created Successfully!")

        st.balloons()

        time.sleep(2)

        st.switch_page("pages/2_Login.py")

     else:

        st.error("⚠ Username already exists.")