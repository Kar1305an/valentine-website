import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine 💘", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background-color: #fff0f5;
    text-align: center;
    font-family: 'Comic Sans MS', cursive;
}

h1 {
    font-size: 48px;
    color: #d63384;
}

#container {
    position: relative;
    height: 350px;
    margin-top: 40px;
}

button {
    font-size: 24px;
    padding: 12px 26px;
    border-radius: 14px;
    border: none;
    cursor: pointer;
}

#yes {
    background-color: #ff4d6d;
    color: white;
}

#no {
    background-color: #adb5bd;
    color: black;
    position: absolute;
    left: 60%;
    top: 50%;
}

#teddy {
    display: none;
    margin-top: 30px;
}
</style>
</head>

<body>

<h1>Will you be my Valentine? 💖</h1>

<div id="container">
    <button id="yes" onclick="showTeddy()">Yes 💕</button>
    <button id="no" onmouseover="moveButton()">No 💔</button>
</div>

<div id="teddy">
    <img src="https://i.imgur.com/8RKXAIV.png" width="280"/>
    <h2>Yay! You said YES 💐💖</h2>
</div>

<script>
function moveButton() {
    const noBtn = document.getElementById("no");
    const maxX = 300;
    const maxY = 200;
    const x = Math.random() * maxX;
    const y = Math.random() * maxY;
    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
}

function showTeddy() {
    document.getElementById("container").style.display = "none";
    document.getElementById("teddy").style.display = "block";
}
</script>

</body>
</html>
"""

components.html(html_code, height=650)
