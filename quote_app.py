import streamlit as st
import random
import time

st.set_page_config(page_title="BB 잭팟 카지노", page_icon="🎰")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #1a1a1a, #000); color: #fff; height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; }
    .main-title { font-size: 50px; color: #FFD700; text-shadow: 0 0 10px #FFD700; }
    .slot-container { display: flex; justify-content: center; gap: 15px; margin: 20px 0; }
    .slot-item { font-size: 60px; background: #222; border: 5px solid #FFD700; border-radius: 10px; width: 100px; height: 100px; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 15px #FFD700; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🎰 JESSE'S SLOT</h1>", unsafe_allow_html=True)

symbols = ["🧪", "💸", "🍗", "🕶️", "🚗", "💎"]
insults = ["겨우 그 정도냐?", "루저, 돈 더 긁어와!", "우리 할머니가 돌려도 이것보단 잘해!", "운도 지지리도 없지."]

WIN_GIF = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW5tMjQxNTN3OXVidXR6OWptd2JubTNsdndiZW54d2hhODh3eTgwaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QCKlfpNs03Yn0AME9E/giphy.gif"
LOSE_GIF = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXppM2R0bm0xaWVuZ2MybGxpdWs4d2hkODFid2piNWFrM3dqaHBpMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YVMmMqAhNbJMQTzOMV/giphy.gif"

slot_placeholder = st.empty()
slot_placeholder.markdown("<div class='slot-container'><div class='slot-item'>❓</div><div class='slot-item'>❓</div><div class='slot-item'>❓</div></div>", unsafe_allow_html=True)

if st.button("내 인생 건다 (ALL IN)"):
    start_time = time.time()
    while time.time() - start_time < 5:
        s1, s2, s3 = random.choice(symbols), random.choice(symbols), random.choice(symbols)
        # f-string 줄바꿈 없이 한 줄로 처리하여 안전하게 작성
        slot_placeholder.markdown(f"<div class='slot-container'><div class='slot-item'>{s1}</div><div class='slot-item'>{s2}</div><div class='slot-item'>{s3}</div></div>", unsafe_allow_html=True)
        time.sleep(0.1)

    r1, r2, r3 = random.choice(symbols), random.choice(symbols), random.choice(symbols)
    slot_placeholder.markdown(f"<div class='slot-container'><div class='slot-item'>{r1}</div><div class='slot-item'>{r2}</div><div class='slot-item'>{r3}</div></div>", unsafe_allow_html=True)
