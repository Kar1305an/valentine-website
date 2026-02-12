import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine 💘", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>

/* ===== BACKGROUND ===== */
body {
    margin: 0;
    padding: 0;
    min-height: 100vh;
    font-family: 'Comic Sans MS', cursive;
    background-image: url('https://pics.coloringsai.com/a-giant-teddy-bear-holding-a-bouquet-of-flowers-and-a-love-note-a-fun-valentines-day-coloring-page-for-kids-and-adults-coloring-page-1738318937022.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    overflow-x: hidden;
}

/* ===== OVERLAY ===== */
.content {
    min-height: 100vh;
    text-align: center;
    background-color: rgba(255, 240, 245, 0.75);
    padding-top: 30px;
}

/* ===== HEADER ===== */
h1 {
    font-size: 46px;
    color: #d63384;
    margin-bottom: 20px;
    letter-spacing: 1px;
    text-shadow: 0 2px 6px rgba(0,0,0,0.15);
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
    box-shadow: 0 0 0 rgba(255, 77, 109, 0.0);
}

#yes:hover {
    box-shadow: 0 0 20px rgba(255, 77, 109, 0.7);
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

/* ===== RESULT ===== */
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
    color: #ff6b81;
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

<h1>Orishalol, will you be my Valentine? 💖</h1>

<div id="container">
    <button id="yes" onclick="showResult()">Yes 💕</button>
    <button id="no" onclick="noClicked()">No 💔</button>
</div>

<div id="result">
    <img src="https://i1.fnp.com/images/pr/uae/l/v20220829125106/mesmerising-flowers-and-chocolates-bouquet-with-teddy-bear_1.jpg"
         width="340"/>
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
