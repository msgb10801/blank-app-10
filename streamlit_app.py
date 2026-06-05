import streamlit as st

# 앱 제목
st.title("🍿 영화관 세트메뉴 조합기")

# 원본 데이터 구조 보존
popcorn = ['기본', '캐러멜', '어니언']
drink = ['콜라', '사이다']

st.subheader("생성된 세트메뉴 목록")

# 원본 반복문 logic 그대로 사용 (print 대신 st.write)
for pop in popcorn:
    for dr in drink:
        st.write(f'🎬 세트메뉴: {pop} 팝콘, {dr}')
