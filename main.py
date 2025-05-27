import streamlit as st
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# 데이터 준비
data = {
    "학교명": ["서초고등학교", "반포고등학교", "양재고등학교"],
    "위도": [37.4833, 37.4950, 37.4762],
    "경도": [127.0327, 127.0156, 127.0321]
}
df = pd.DataFrame(data)

st.title("서울 서초구 고등학교 위치 지도")

# Folium 지도 생성 (서초구 중심)
m = folium.Map(location=[37.4833, 127.0327], zoom_start=13)

# 고등학교 마커 추가
for idx, row in df.iterrows():
    folium.Marker(
        location=[row["위도"], row["경도"]],
        popup=row["학교명"],
        icon=folium.Icon(color='blue', icon='graduation-cap', prefix='fa')
    ).add_to(m)

# Streamlit에 Folium 지도 출력
st_folium(m, width=700, height=500)
