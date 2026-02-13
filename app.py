import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine 💘", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>

/* ===== CLEAN GRADIENT BACKGROUND ===== */
body {
    margin: 0;
    padding: 0;
    min-height: 100vh;
    font-family: 'Comic Sans MS', cursive;
    background: linear-gradient(135deg, #ffe6f0, #ffd6e8, #ffcce0);
    overflow-x: hidden;
}

/* ===== CONTENT LAYER ===== */
.content {
    min-height: 100vh;
    text-align: center;
    padding-top: 40px;
}

/* ===== HEADER ===== */
h1 {
    font-size: 46px;
    color: #d63384;
    margin-bottom: 20px;
    letter-spacing: 1px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* ===== BUTTON AREA ===== */
#container {
    position: relative;
    height: 420px;
    margin-top: 40px;
}

button {
    border-radius: 16px;
    border: none;
    cursor: pointer;
    position: absolute;
    transition: all 0.3s ease;
}

/* YES BUTTON */
#yes {
    background-color: #ff4d6d;
    color: white;
    left: 38%;
    top: 45%;
    font-size: 26px;
    padding: 14px 32px;
}

#yes:hover {
    box-shadow: 0 0 20px rgba(255, 77, 109, 0.6);
    transform: scale(1.05);
}

/* NO BUTTON */
#no {
    background-color: #adb5bd;
    color: black;
    left: 55%;
    top: 55%;
    font-size: 24px;
    padding: 12px 26px;
}

/* ===== RESULT IMAGE ===== */
#result {
    display: none;
    margin-top: 30px;
    animation: fadeInScale 0.8s ease forwards;
}

@keyframes fadeInScale {
    from {
        opacity: 0;
        transform: scale(0.85);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

/* ===== FLOATING HEARTS ===== */
.heart {
    position: fixed;
    bottom: -10px;
    font-size: 22px;
    animation: floatUp 6s linear infinite;
    opacity: 0.7;
}

@keyframes floatUp {
    from {
        transform: translateY(0) translateX(0);
        opacity: 0.7;
    }
    to {
        transform: translateY(-110vh) translateX(30px);
        opacity: 0;
    }
}

</style>
</head>

<body>

<!-- FLOATING HEARTS -->
<span class="heart" style="left: 10%; animation-delay: 0s;">💖</span>
<span class="heart" style="left: 30%; animation-delay: 2s;">💕</span>
<span class="heart" style="left: 50%; animation-delay: 1s;">💗</span>
<span class="heart" style="left: 70%; animation-delay: 3s;">💘</span>
<span class="heart" style="left: 90%; animation-delay: 1.5s;">❤️</span>

<div class="content">

<h1>orishalol, will you be my valentine? 💖</h1>

<div id="container">
    <button id="yes" onclick="showResult()">Yes 💕</button>
    <button id="no" onclick="noClicked()">No 💔</button>
</div>

<div id="result">
    <img src="https://i.imgur.com/8RKXAIV.png" width="340"/>

    <h2>I knew you’d say yes 🧸💐🍫</h2>
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

components.html(html_code, height=1000)
