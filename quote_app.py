import streamlit as st
import random
import time

st.set_page_config(page_title="BB 잭팟 카지노", page_icon="🎰")

# 핵심 CSS: 화면 전체 정중앙 정렬
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #1a1a1a, #000);
        color: #fff;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center; /* 세로 축 정중앙 */
        align-items: center;     /* 가로 축 정중앙 */
    }
    .main-title { font-size: 50px; color: #FFD700; text-shadow: 0 0 10px #FFD700; margin-bottom: 20px; }
    .slot-container { display: flex; justify-content: center; gap: 15px; margin: 20px 0; }
    .slot-item { font-size: 60px; background: #222; border: 5px solid #FFD700; border-radius: 10px; width: 100px; height: 100px; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 15px #FFD700; }
    .win-text { font-size: 40px; color: #00FF00; margin-top: 10px; }
    .lose-text { font-size: 25px; color: #FF4B4B; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

# 화면 구성
st.markdown("<h1 class='main-title'>🎰 JESSE'S SLOT</h1>", unsafe_allow_html=True)

# 브레이킹 배드 상징 아이콘들
symbols = ["🧪", "💸", "🍗", "🕶️", "🚗", "💎"]
# 독한 놀림 멘트들
insults = ["겨우 그 정도냐?", "루저, 돈 더 긁어와!", "우리 할머니가 돌려도 이것보단 잘해!", "운도 지지리도 없지."]

# 슬롯 박스를 담을 빈 공간
slot_placeholder = st.empty()

# 초기 상태 (물음표 3개)
slot_placeholder.markdown("""
    <div class='slot-container'>
        <div class='slot-item'>❓</div>
        <div class='slot-item'>❓</div>
        <div class='slot-item'>❓</div>
    </div>
""", unsafe_allow_html=True)

# 버튼 (세로 축 가운데)
if st.button("내 인생 건다 (ALL IN)"):
    start_time = time.time()
    while time.time() - start_time < 5:  # 5초간 회전 연출
        s1, s2, s3 = random.choice(symbols), random.choice(symbols), random.choice(symbols)
        slot_placeholder.markdown(f"""
            <div class='slot-container'>
                <div class='slot-item'>{s1}</div>
                <div class='slot-item'>{s2}</div>
                <div class='slot-item'>{s3}</div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(0.1)

    # 최종 결과 판정
    res1, res2, res3 = random.choice(symbols), random.choice(symbols), random.choice(symbols)
    # 테스트용: 무조건 성공하게 하려면 아래 주석 해제
    # res1 = res2 = res3 = "💎"

    slot_placeholder.markdown(f"""
        <div class='slot-container'>
            <div class='slot-item'>{res1}</div>
            <div class='slot-item'>{res2}</div>
            <div class='slot-item'>{res3}</div>
        </div>
    """, unsafe_allow_html=True)

    if res1 == res2 == res3:
        st.balloons()
        st.markdown
