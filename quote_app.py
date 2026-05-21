import streamlit as st
import random
import time

st.set_page_config(page_title="BB 슬롯머신", page_icon="🎰")

# 건방진 멘트 리스트
insults = ["겨우 그 정도냐?", "운도 실력이야, 요.", "내 얼굴 보고도 그게 나와?", "더 분발해봐, 루저.", "아직 멀었어."]

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #FFD700; text-align: center; }
    .slot { font-size: 50px; border: 5px solid #FFD700; padding: 20px; margin: 10px; }
    .neon { text-shadow: 0 0 10px #FFD700, 0 0 20px #FFD700; }
    </style>
""", unsafe_allow_html=True)

st.title("🎰 Breaking Bad CASINO")
symbols = ["🧪", "💸", "🍗", "🕶️", "🚗"]

if st.button("돌려, YO!"):
    # 1. 돌아가는 모션 (빠르게 5번 교체)
    slot_placeholder = st.empty()
    for _ in range(5):
        with slot_placeholder.container():
            c1, c2, c3 = st.columns(3)
            c1.markdown(f"<div class='slot'>{random.choice(symbols)}</div>", unsafe_allow_html=True)
            c2.markdown(f"<div class='slot'>{random.choice(symbols)}</div>", unsafe_allow_html=True)
            c3.markdown(f"<div class='slot'>{random.choice(symbols)}</div>", unsafe_allow_html=True)
        time.sleep(0.1)

    # 2. 결과 추출
    s1, s2, s3 = random.choice(symbols), random.choice(symbols), random.choice(symbols)
    
    with slot_placeholder.container():
        c1, c2, c3 = st.columns(3)
        c1.markdown(f"<div class='slot'>{s1}</div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='slot'>{s2}</div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='slot'>{s3}</div>", unsafe_allow_html=True)

    # 3. 결과 판정
    if s1 == s2 == s3:
        st.balloons()
        st.markdown("<h1 class='neon'>JACKPOT! 제국을 건설할 시간이다!</h1>", unsafe_allow_html=True)
    else:
        st.error(random.choice(insults))
