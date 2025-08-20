import streamlit as st
import random

# 샘플 맛집/명소 데이터
travel_data = {
    "서울": {
        "맛집": ["광장시장 빈대떡", "을지로 골뱅이", "망원동 카페거리", "한남동 파스타집"],
        "명소": ["경복궁", "남산타워", "홍대거리", "롯데월드타워"]
    },
    "부산": {
        "맛집": ["자갈치시장 회센터", "밀면 맛집", "돼지국밥 골목", "해운대 카페"],
        "명소": ["해운대 해수욕장", "광안리", "감천문화마을", "태종대"]
    },
    "제주": {
        "맛집": ["흑돼지 거리", "갈치조림 식당", "성산일출봉 근처 카페", "오메기떡집"],
        "명소": ["성산일출봉", "협재해수욕장", "우도", "한라산"]
    }
}

# Streamlit UI
st.title("✈️ AI 여행 플래너")
st.write("여행지를 입력하면 맛집과 명소 중심의 일정을 추천해드립니다!")

# 사용자 입력
destination = st.text_input("여행지를 입력하세요 (예: 서울, 부산, 제주):")

days = st.slider("여행 일수", 1, 5, 2)

if st.button("여행 일정 짜기"):
    if destination in travel_data:
        st.subheader(f"📍 {destination} 여행 {days}일 추천 플랜")

        for day in range(1, days+1):
            st.markdown(f"### Day {day}")
            food = random.choice(travel_data[destination]["맛집"])
            place = random.choice(travel_data[destination]["명소"])
            
            st.write(f"- 🍴 추천 맛집: **{food}**")
            st.write(f"- 🏖️ 추천 명소: **{place}**")
            st.divider()
    else:
        st.error("데이터에 없는 여행지입니다. (서울, 부산, 제주 중 입력해주세요)")
