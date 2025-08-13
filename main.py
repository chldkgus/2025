import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 패션 추천", page_icon="👗", layout="wide")

# CSS 스타일 적용 (이미지와 텍스트를 화려하게)
st.markdown("""
    <style>
        .title {
            font-size: 48px;
            font-weight: bold;
            color: #FF4081;
            text-align: center;
            padding-bottom: 20px;
        }
        .subtitle {
            font-size: 24px;
            color: #555;
            text-align: center;
            margin-top: 10px;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px 0;
        }
        .description {
            font-size: 18px;
            color: #444;
            text-align: center;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="title">✨ MBTI 기반 트렌디 패션 추천 ✨</div>', unsafe_allow_html=True)

# MBTI 목록
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI별 패션 추천 데이터
mbti_fashion = {
    "ISTJ": ("클래식 셋업 슈트", "https://i.pinimg.com/736x/0b/87/91/0b8791f95f184659903c94a2b8c3a7cd.jpg"),
    "ISFJ": ("모던 단정 원피스", "https://i.pinimg.com/736x/ab/6a/93/ab6a931f74cb28c2f45c4d3a8d1a5c53.jpg"),
    "INFJ": ("빈티지 감성 코트", "https://i.pinimg.com/736x/b1/43/d4/b143d4968cbf56d5bb0dd88e6e0c90c2.jpg"),
    "INTJ": ("블랙 미니멀 자켓", "https://i.pinimg.com/736x/2c/cd/4d/2ccd4d45908bfbf61b884e3d0bdf7f92.jpg"),
    "ISTP": ("아메카지 워크웨어", "https://i.pinimg.com/736x/90/f0/46/90f04620e2d52d64b23e3a038f9c13a5.jpg"),
    "ISFP": ("보헤미안 패턴 셔츠", "https://i.pinimg.com/736x/43/2f/89/432f8934ed24d7e21a3e78a69b9c3e88.jpg"),
    "INFP": ("파스텔 니트 & 청바지", "https://i.pinimg.com/736x/8b/25/c0/8b25c086c0ddc4696a379cb0af07d41e.jpg"),
    "INTP": ("심플 스웨트셔츠", "https://i.pinimg.com/736x/1a/dc/71/1adc71f65d0dfeb8d27a06600a4f6324.jpg"),
    "ESTP": ("스트리트 오버사이즈 후드", "https://i.pinimg.com/736x/ed/1b/cd/ed1bcd4c25de579ebc9b0e7cfe6d22b2.jpg"),
    "ESFP": ("유니크 컬러풀 재킷", "https://i.pinimg.com/736x/c6/f8/9b/c6f89b6eb6ff859c1323e4a55f7cc30a.jpg"),
    "ENFP": ("캐주얼 오버롤", "https://i.pinimg.com/736x/4a/6c/6e/4a6c6e5a2c95e4b2c48f3d9c0b1b35ee.jpg"),
    "ENTP": ("모던 셋업 + 스니커즈", "https://i.pinimg.com/736x/16/c4/5b/16c45b6c40c1ef6af31872897c05f1bc.jpg"),
    "ESTJ": ("비즈니스 캐주얼 셔츠", "https://i.pinimg.com/736x/8f/f7/85/8ff7853d6d3f038f04c24c8652cf7b45.jpg"),
    "ESFJ": ("페미닌 블라우스", "https://i.pinimg.com/736x/f5/65/76/f565767d829b30f7a44537006e4f75c2.jpg"),
    "ENFJ": ("심플 모던 원피스", "https://i.pinimg.com/736x/f3/1e/cd/f31ecd814e3c77d0152c5f3b57c6e606.jpg"),
    "ENTJ": ("파워 슈트 스타일", "https://i.pinimg.com/736x/c9/52/80/c95280bb60f28d1ff6d235b5e152f2a0.jpg")
}

# 선택 박스
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# 결과 표시
if selected_mbti:
    fashion_name, fashion_img = mbti_fashion[selected_mbti]
    st.markdown(f'<div class="subtitle">💡 {selected_mbti} 유형을 위한 트렌디 패션: <b>{fashion_name}</b></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="image-container"><img src="{fashion_img}" width="600"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="description">MBTI <b>{selected_mbti}</b> 성향에 맞춘 스타일입니다.<br>'
                f'트렌드를 따라가면서도 자신만의 개성을 표현해 보세요!</div>', unsafe_allow_html=True)
