import streamlit as st
import json
import random

# 페이지 설정
st.set_page_config(page_title="BrB", page_icon="⚡")

# CSS로 힙한 스타일링 (폰트 + 배경 노이즈)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    .stApp { 
        background-color: #000; 
        color: #ADFF2F;
        font-family: 'Press Start 2P', cursive;
    }
    
    /* 배경 노이즈 효과 */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
        opacity: 0.2;
        pointer-events: none;
    }

    .quote-box { 
        border: 4px solid #ADFF2F; 
        padding: 40px; 
        margin-top: 50px;
        text-align: center; 
        box-shadow: 0 0 20px #ADFF2F;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ 오늘의 명언이다 쨔샤")

try:
    with open('quotes.json', 'r', encoding='utf-8') as f:
        quotes = json.load(f)
except:
    quotes = [{"text": "데이터가 없다, YO.", "author": "제시"}]

quote = random.choice(quotes)

st.markdown(f"""
    <div class="quote-box">
        <h3>"{quote['text']}"</h3>
        <p style="font-size: 0.8em; margin-top: 20px;">- {quote['author']} -</p>
    </div>
""", unsafe_allow_html=True)

if st.button("문장띠로리"):
    st.rerun()

st.markdown("---")
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJ6eXN0eG5qN3J6eXN0eG5qN3J6eXN0eG5qN3J6eXN0eG5qJmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKVUn7iM8FMEU24/giphy.gif")
