import streamlit as st
import random

st.set_page_config(page_title="Valentine 💘", layout="wide")

# Initialize session state
if "yes_clicked" not in st.session_state:
    st.session_state.yes_clicked = False

if "no_scale" not in st.session_state:
    st.session_state.no_scale = 1.0

if "yes_scale" not in st.session_state:
    st.session_state.yes_scale = 1.0

# Background & hearts via CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffe6f0, #ffd6e8, #ffcce0);
}
.big-font {
    font-size: 46px !important;
    color: #d63384;
    text-align: center;
}
div.stButton > button {
    border-radius: 16px;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

# Floating hearts
st.markdown("""
<div style="position:fixed; bottom:0; left:10%; font-size:22px;">💖</div>
<div style="position:fixed; bottom:0; left:30%; font-size:22px;">💕</div>
<div style="position:fixed; bottom:0; left:50%; font-size:22px;">💗</div>
<div style="position:fixed; bottom:0; left:70%; font-size:22px;">💘</div>
<div style="position:fixed; bottom:0; left:90%; font-size:22px;">❤️</div>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Orishalol, will you be my Valentine? 💖</p>', unsafe_allow_html=True)

if not st.session_state.yes_clicked:

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes 💕"):
            st.session_state.yes_clicked = True

    with col2:
        if st.button("No 💔"):
            # Shrink No
            st.session_state.no_scale -= 0.1
            if st.session_state.no_scale < 0.3:
                st.session_state.no_scale = 0.3

            # Grow Yes
            st.session_state.yes_scale += 0.1

            st.rerun()

else:
    st.image("teddy.jpeg", width=350)
    st.markdown("### I knew you'd say yes 🧸💐🍫")
