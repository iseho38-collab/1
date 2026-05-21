import streamlit as st
import random
import time

st.set_page_config(page_title="BB 잭팟 카지노", page_icon="🎰")

# CSS를 아주 깔끔하게 정리했습니다.
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #1a1a1a, #000); color: #fff; text-align: center; font-family: sans-serif; }
    .main-title { font-size: 60px; color: #FFD700; text-shadow: 0 0 20px #FFD700; margin-bottom: 20px; }
    .slot-container { display: flex; justify-content: center; gap: 10px; margin: 30px 0; }
    .slot-item { font-size: 80px; background: #222; border: 5px solid #FFD700; border-radius: 10px; width: 120px; height: 120px; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 20px #FFD700; }
    .win-text { font-size: 50px; color: #00FF00; margin-top: 20px; }
    .lose-text { font-size: 30px; color: #FF4B4B; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🎰 JESSE'S SLOT</h1>", unsafe_allow_html=True)

symbols = ["🧪", "💸", "🍗", "🕶️", "🚗", "💎"]
insults = ["겨우 그 정도냐?", "루저, 돈 더 긁어와!", "우리 할머니가 돌려도 이것보단 잘해!", "운도 지지리도 없지."]

if st.button("내 인생 건다 (ALL IN)"):
    slot_placeholder = st.empty()
    start_time = time.time()
    
    # 5초간 회전 연출
    while time.time() - start_time < 5:
        s1, s2, s3 = random.choice(symbols), random.choice(symbols), random.choice(symbols)
        slot_placeholder.markdown(f"""
            <div class='slot-container'>
                <div class='slot-item'>{s1}</div>
                <div class='slot-item'>{s2}</div>
                <div class='slot-item'>{s3}</div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(0.1)

    # 최종 결과
    res1, res2, res3 = random.choice(symbols), random.choice(symbols), random.choice(symbols)
    slot_placeholder.markdown(f"""
        <div class='slot-container'>
            <div class='slot-item'>{res1}</div>
            <div class='slot-item'>{res2}</div>
            <div class='slot-item'>{res3}</div>
        </div>
    """, unsafe_allow_html=True)

    if res1 == res2 == res3:
        st.balloons()
        st.markdown("<p class='win-text'>💎 JACKPOT!!! 제국은 네 것이다! 💎</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p class='lose-text'>{random.choice(insults)}</p>", unsafe_allow_html=True)
