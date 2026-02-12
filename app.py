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
    font-size: 50px;
    color: #d63384;
    margin-top: 20px;
}

#container {
    position: relative;
    height: 420px;
    margin-top: 50px;
}

button {
    border-radius: 14px;
    border: none;
    cursor: pointer;
    position: absolute;
    transition: all 0.25s ease;
}

#yes {
    background-color: #ff4d6d;
    color: white;
    left: 38%;
    top: 45%;
    font-size: 26px;
    padding: 14px 30px;
}

#no {
    background-color: #adb5bd;
    color: black;
    left: 55%;
    top: 55%;
    font-size: 24px;
    padding: 12px 26px;
}

#teddy {
    display: none;
    margin-top: 40px;
}
</style>
</head>

<body>

<h1>orishalol will you be my vallentine? 💖</h1>

<div id="container">
    <button id="yes" onclick="showTeddy()">Yes 💕</button>
    <button id="no" onclick="noClicked()">No 💔</button>
</div>

<div id="teddy">
    <img src="https://i.imgur.com/4M7IWwP.png" width="320"/>
    <h2>You had no choice anyway 😄💐🍫</h2>
</div>

<script>
let noScale = 1.0;
let yesScale = 1.0;

function noClicked() {
    const noBtn = document.getElementById("no");
    const yesBtn = document.getElementById("yes");

    noScale -= 0.12;
    yesScale += 0.12;

    if (noScale < 0.2) {
        noScale = 0.2;
    }

    noBtn.style.transform = "scale(" + noScale + ")";
    yesBtn.style.transform = "scale(" + yesScale + ")";

    const x = Math.random() * 300;
    const y = Math.random() * 220;
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

components.html(html_code, height=750)
