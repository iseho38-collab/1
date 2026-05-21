import streamlit as st
import random
import time

st.set_page_config(page_title="Breaking Bad Slot", page_icon="🎰")

# 슬롯 아이콘
symbols = ["🧪", "💸", "🍗", "🕶️", "🚗"]

st.title("🎰 Breaking Bad Slot")

if st.button("돌려라, YO!"):
    # 3개 랜덤 추출
    slot1 = random.choice(symbols)
    slot2 = random.choice(symbols)
    slot3 = random.choice(symbols)
    
    # 결과 보여주기 (힙하게 표현)
    col1, col2, col3 = st.columns(3)
    col1.metric("1", slot1)
    col2.metric("2", slot2)
    col3.metric("3", slot3)
    
    # 잭팟 판별
    if slot1 == slot2 == slot3:
        st.balloons() # 축하 폭죽
        st.success("잭팟이다! 제국을 건설할 시간이야!")
        st.video("https://www.youtube.com/watch?v=k4K23W31v4Q") # 월터의 웃음 영상 등
    else:
        st.error("꽝이야. 다시 도전해.")

st.markdown("---")
st.write("3개가 일치하면 잭팟입니다.")
