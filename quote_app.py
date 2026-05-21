import streamlit as st
import random
import time
import os # 파일 존재 확인을 위해 추가

st.set_page_config(page_title="BB 잭팟 카지노", page_icon="🎰")

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #1a1a1a, #000);
        color: #fff;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .main-title { font-size: 50px; color: #FFD700; text-shadow: 0 0 10px #FFD700; }
    .slot-container { display: flex; justify-content: center; gap: 15px; margin: 20px 0; }
    .slot-item { font-size: 60px; background: #222; border: 5px solid #FFD700; border-radius: 10px; width: 100px; height: 100px; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 15px #FFD700; font-family: sans-serif; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🎰 JESSE'S SLOT</h1>", unsafe_allow_html=True)

symbols = ["🧪", "💸", "🍗", "🕶️", "🚗", "💎"]
insults = ["겨우 그 정도냐?", "루저, 돈 더 긁어와!", "우리 할머니가 돌려도 이것보단 잘해!", "운도 지지리도 없지."]

slot_placeholder = st.empty()

# 초기 상태
slot_placeholder.markdown("<div class='slot-container'><div class='slot-item'>❓</div><div class='slot-item'>❓</div><div class='slot-item'>❓</div></div>", unsafe_allow_html=True)

if st.button("내 인생 건다 (ALL IN)"):
    start_time = time.time()
    while time.time() - start_time < 5:
        s1, s2, s3 = random.choice(symbols), random.choice(symbols), random.choice(symbols)
        slot_placeholder.markdown(f"<div class='slot-container'><div class='slot-item'>{s1}</div><div class='slot-item'>{s2}</div><div class='slot-item'>{s3}</div></div>", unsafe_allow_html=True)
        time.sleep(0.1)

    r1, r2, r3 = random.choice(symbols), random.choice(symbols), random.choice(symbols)
    # 테스트용: 무조건 성공하게 하려면 아래 주석 해제
    # r1 = r2 = r3 = "💎"

    slot_placeholder.markdown(f"<div class='slot-container'><div class='slot-item'>{r1}</div><div class='slot-item'>{r2}</div><div class='slot-item'>{r3}</div></div>", unsafe_allow_html=True)

    if r1 == r2 == r3:
        st.balloons()
        st.markdown("<p style='font-size:30px; color:#00FF00; text-align:center;'>💎 JACKPOT!!! 제국은 네 것이다!</p>", unsafe_allow_html=True)
        # 이미지 전면 배치 스타일 (그림자 효과 추가)
        st.markdown("<style>.stImage img { box-shadow: 0 0 30px rgba(255,255,255,0.7); border-radius:15px; border: 5px solid #fff; }</style>", unsafe_allow_html=True)
        # 저장소에 올린 파일 불러오기
        if os.path.exists('win_walter.png'):
            st.image('win_walter.png', width=300)
        else:
            st.error("이미지 파일을 못 찾았어! 깃허브에 올렸는지 확인해봐.")
    else:
        st.markdown(f"<p style='font-size:20px; color:#FF4B4B; text-align:center;'>{random.choice(insults)}</p>", unsafe_allow_html=True)
        # 이미지 전면 배치 스타일 (그림자 효과 추가)
        st.markdown("<style>.stImage img { box-shadow: 0 0 30px rgba(255,255,255,0.7); border-radius:15px; border: 5px solid #fff; }</style>", unsafe_allow_html=True)
        # 저장소에 올린 파일 불러오기
        if os.path.exists('lose_walter.png'):
            st.image('lose_walter.png', width=300)
        else:
            st.error("이미지 파일을 못 찾았어! 깃허브에 올렸는지 확인해봐.")
