import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine 💘", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
/* FULL PAGE BACKGROUND — ALWAYS PRESENT */
body {
    margin: 0;
    padding: 0;
    min-height: 100vh;
    font-family: 'Comic Sans MS', cursive;
    background-image: url('https://pics.coloringsai.com/a-giant-teddy-bear-holding-a-bouquet-of-flowers-and-a-love-note-a-fun-valentines-day-coloring-page-for-kids-and-adults-coloring-page-1738318937022.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* CONTENT LAYER */
.content {
    min-height: 100vh;
    text-align: center;
    background-color: rgba(255, 240, 245, 0.75); /* soft overlay */
    padding-top: 30px;
}

h1 {
    font-size: 48px;
    color: #d63384;
    margin-bottom: 20px;
}

#container {
    position: relative;
    height: 420px;
    margin-top: 40px;
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

#result {
    display: none;
    margin-top: 30px;
}
</style>
</head>

<body>

<div class="content">

<h1>orishalol will you be my vallentine? 💖</h1>

<div id="container">
    <button id="yes" onclick="showResult()">Yes 💕</button>
    <button id="no" onclick="noClicked()">No 💔</button>
</div>

<div id="result">
    <img src="https://i1.fnp.com/images/pr/uae/l/v20220829125106/mesmerising-flowers-and-chocolates-bouquet-with-teddy-bear_1.jpg"
         width="340"/>
    <h2>You had no choice anyway 😄💐🍫</h2>
</div>

</div>

<script>
let noScale = 1.0;
let yesScale = 1.0;

function noClicked() {
    const noBtn = document.getElementById("no");
    const yesBtn = document.getElementById("yes");

    noScale -= 0.12;
    yesScale += 0.12;

    if (noScale < 0.2) noScale = 0.2;

    noBtn.style.transform = "scale(" + noScale + ")";
    yesBtn.style.transform = "scale(" + yesScale + ")";

    const x = Math.random() * 300;
    const y = Math.random() * 220;
    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
}

function showResult() {
    document.getElementById("container").style.display = "none";
    document.getElementById("result").style.display = "block";
}
</script>

</body>
</html>
"""

components.html(html_code, height=950)
