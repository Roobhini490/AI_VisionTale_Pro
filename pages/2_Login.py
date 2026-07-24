

import streamlit as st
from vision_utils import get_base64
import time
from database import login_user
import vision_utils


bg = get_base64("assets/images/background.png")
st.set_page_config(
    page_title="Login",
    page_icon="📖",
    layout="wide"
)


st.markdown(f"""
<style>

[data-testid="stSidebar"] {{
    display: none;
}}

[data-testid="collapsedControl"] {{
    display: none;
}}

#MainMenu {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

.stApp {{
    background-image: url("data:image/png;base64,{bg}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

</style>
""", unsafe_allow_html=True)


with open("style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )
st.markdown("""
<div class="login-card">

<h1 style="
text-align:center;
font-size:50px;
color:#A8E6A3;
font-family: 'Comic Sans MS', cursive;
margin-bottom:10px;">

Welcome Back!

</h1>

<h3 style="
text-align:center;
color:#D8B4FE;
font-family: 'Comic Sans MS', cursive;            
margin-bottom:30px;">
Continue Your Magical Adventure ✨

</h3>

""", unsafe_allow_html=True)

# Center the login form
left, center, right = st.columns([1, 2, 1])

with center:
    

    st.markdown(
        "<h3 style='text-align:center;color:#2abba5 ;font-family: Comic Sans MS;'>🧚 Welcome Little Explorer!</h3>",
    unsafe_allow_html=True
)
    st.markdown(
        "<h3 style='text-align:center;'>🦄✨</h3>",
    unsafe_allow_html=True
    ) 

    st.markdown("""
       <h3 style="
       color:#e45598;
       font-family:'Comic Sans MS',cursive;
       font-size:30px;
       margin-bottom:5px;
       ">
       👤 Username
       </h3>
       """, unsafe_allow_html=True)

    username = st.text_input(
          "",
        placeholder="Enter your username",
        label_visibility="collapsed",
        key="username"
)
    st.write("")

    st.markdown("""
<h3 style="
color:#e45598;
font-family:'Comic Sans MS',cursive;
font-size:30px;
margin-bottom:5px;
">
🔒 Password
</h3>
""", unsafe_allow_html=True)

    password = st.text_input(
       "",
     placeholder="Enter your password",
     type="password",
     label_visibility="collapsed",
     key="password"
)
st.write("")


# Center the buttons
left, center, right = st.columns([1.7, 2, 1])

with center:
    if st.button("🌟 Log In", use_container_width=True):

        if username.strip() == "":
          st.error("Please enter your username.")

        elif password.strip() == "":
          st.error("Please enter your password.")

        else:
 
          user = login_user(username, password)

          if user:
            
            st.success("🌈 Welcome Back!")
            st.balloons()

            time.sleep(2)
            st.switch_page("pages/4_Upload_Image.py")

          else:

              st.error("❌ Invalid Username or Password")

left, center, right = st.columns([1, 2, 1])

with center:
    st.markdown(
        """
        <div style="text-align:center;">
            <p style="
                color:#cb34c9;
                font-size:18px;
                font-family:'Comic Sans MS', cursive;
                margin-bottom:8px;
            ">
                New to AI VisionTale?
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
left, center, right = st.columns([1.7, 2, 1])

with center:
    if st.button("✨ Create Account", use_container_width=True):
        st.switch_page("pages/3_Create_Account.py")

    