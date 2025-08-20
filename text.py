import streamlit as st
import random

# 샘플 데이터
travel_data = {
    "서울": {
        "맛집": ["광장시장 빈대떡", "을지로 골뱅이", "망원동 카페거리", "한남동 파스타집", "삼청동 한식집"],
        "명소": ["경복궁", "남산타워", "홍대거리", "롯데월드타워", "북촌한옥마을"]
    },
    "부산": {
        "맛집": ["자갈치시장 회센터", "밀면 맛집", "돼지국밥 골목", "해운대 카페", "동래 파전집"],
        "명소": ["해운대 해수욕장", "광안리", "감천문화마을", "태종대", "송정 해수욕장"]
    },
    "제주": {
        "맛집": ["흑돼지 거리", "갈치조림 식당", "성산일출봉 카페", "오메기떡집", "전복죽 맛집"],
        "명소": ["성산일출봉", "협재해수욕장", "우도", "한라산", "용머리해안"]
    }
}

# 기본 추천 (데이터 없는 경우)
default_foods = ["지역 전통시장", "로컬 식당", "핫한 카페", "현지 유명 분식집"]
default_places = ["도심 산책", "박물관", "랜드마크", "전망대", "공원"]

# HTML 카드 템플릿
def create_card(title, items):
    card_html = f"""
    <div style="
        background-color:#f8f9fa;
        padding:15px;
        border-radius:15px;
        box-shadow:2px 2px 8px rgba(0,0,0,0.1);
        margin-bottom:15px;">
        <h4 style="color:#2c3e50;">{title}</h4>
        <ul style="margin:0; padding-left:20px; color:#34495e;">
    """
    for i in items:
        card_html += f"<li>{i}</li>"
    card_html += "</ul></div>"
    return card_html

# Streamlit UI
st.title("✨ AI 여행 플래너")
st.write("여행지를 입력하면 **맞춤형 맛집 + 명소 일정표**를 자동 생성해드립니다!")

# 입력
destination = st.text_input("📍 여행지를 입력하세요 (예: 서울, 부산, 제주, 또는 다른 도시도 가능):")
days = st.slider("🗓️ 여행 일수", 1, 5, 2)

if st.button("✈️ 여행 일정 짜기"):
    if destination.strip() == "":
        st.error("여행지를 입력해주세요!")
    else:
        st.subheader(f"📌 {destination} {days}일 추천 일정표")

        # 여행지 데이터 불러오기 (없으면 기본 리스트 사용)
        foods = travel_data.get(destination, {}).get("맛집", default_foods)
        places = travel_data.get(destination, {}).get("명소", default_places)

        for day in range(1, days + 1):
            st.markdown(f"## 🌞 Day {day}")

            # 하루 일정을 아침, 점심, 오후, 저녁으로 나눔
            schedule = {
                "아침": random.choice(places),
                "점심": random.choice(foods),
                "오후": random.choice(places),
                "저녁": random.choice(foods)
            }

            # 카드로 보여주기
            for time, place in schedule.items():
                st.markdown(
                    create_card(f"🕑 {time}", [place]),
                    unsafe_allow_html=True
                )

            st.markdown("---")
