import streamlit as st
import random
import time

# 1. 페이지 설정 및 디자인 (가운데 정렬 + 반짝이는 애니메이션)
st.set_page_config(page_title="BB 잭팟 카지노", page_icon="🎰")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');

    /* 배경: 화려한 다크 카지노 느낌 */
    .stApp {
        background: radial-gradient(circle, #1a1a1a, #000);
        color: #fff;
        font-family: 'Black Han Sans', sans-serif;
        text-align: center;
    }

    /* 제목 & 버튼 가운데 정렬 */
    .main-title { font-size: 80px; color: #FFD700; text-shadow: 0 0 20px #FFD700; margin-bottom: 20px; }
    
    /* 슬롯 박스 디자인 */
    .slot-container {
        display: flex; justify-content: center; gap: 20px; margin: 50px 0;
    }
    .slot-item {
        font-size: 100px; background: #222; border: 8px solid #FFD700;
        border-radius: 15px; width: 180px; height: 180px;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 0 30px #FFD700;
    }

    /* 성공 시 반짝거리는 애니메이션 */
    @keyframes sparkle {
        0% { filter: brightness(1); transform: scale(1); }
        50% { filter: brightness(2.5); transform: scale(1.1); text-shadow: 0 0 50px #fff; }
        100% { filter: brightness(1); transform: scale(1); }
    }
    .win-text {
        font-size: 60px; color: #00FF00; animation: sparkle 0.5s infinite;
        margin-top: 30px;
    }

    /* 실패 시 문구 스타일 */
    .lose-text { font-size: 40px; color: #FF4B4B; margin-top: 30px; }
    
    /* 버튼 커스텀 (가운데 정렬용 CSS) */
    div.
