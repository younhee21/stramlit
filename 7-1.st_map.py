import numpy as np
import pandas as pd 
import streamlit as st

# 위도 : latitude  경도 : longitude
data = pd.DataFrame({
    'lat':[-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
    'lon':[-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5]
})

# 지도 그리기
st.map(data,
       latitude='lat',
       longitude='lon')


##################### 연습 문제 #####################

# 1. 아래 데이터를 딕셔너리 형태로 선언하고 map_data에 저장하기 
# 'lat': -34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97
# 'lon': -58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5
# 'name': 'Buenos Aires', 'Paris', 'melbourne', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador'
# 'value': 10, 12, 40, 70, 23, 43, 100, 43

map_data = pd.DataFrame({
    'lat': [-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
    'lon': [-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
    'name': ['Buenos Aires', 'Paris', 'melbourne', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador'],
    'value': [10, 12, 40, 70, 23, 43, 100, 43]})




# 2. subheader 코드를 사용하여 지도 제목 'Aivle Map' 보여주기
st.subheader('Aivle Map')

# 3. checkbox를 이용하여 checkbox를 선택여부에 따라
#    write 코드를 사용하여 화면에 데이터프레임 값 나타내기
if st.checkbox('Display Data?'):
    st.write(map_data)

# 지도 그리기
st.map(map_data, latitude='lat', longitude='lon')


# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\7-1.st_map.py