import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px

st.title('심화문제')

st.subheader('1. Altair Scatter chart- 재무 분석')

#### https://raw.githubusercontent.com/huhshin/streamlit/master/data_financial.csv 읽어오기 
#### 한글 encoding='CP949'

# fi = 

#### 체크박스 버튼을 선택하여 데이터 확인

# if st. ('재무분석 데이터 조회'):
#     st.

    
##### radio button을 사용하여 '판매량', '매출원가', '수익'을 선택

# sel = st. (
#      '총매출 대비 분석을 원하는 항목을 선택하세요.',
#        )


##### altar circle chart 그리기: x=총매출, y=선택된 항목, color='상품', size=선택된 항목

# fig = alt.

# st.


st.subheader('2. Plotly Pie chart- 타이타닉 생존 분석')

#### https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv 데이터 읽어오기 
titanic = 

##### 체크박스 버튼을 선택하여 데이터 확인
if st.
    st.

#####  select box를 사용하여 탑승지역-Embarked, 객실등급-Pclass 선택

tit = st.
     '생존자 분석을 위한 항목을 선택하세요.',
      )
if tit == 
    sel =




#####  columns 함수를 이용하여 좌-pie chart, 우-bar chart 그리기
#####  차트 크기 조정- fig.update_layout(height=400, width=400)

col1, col2 = st.
with col1:
    # pie chart 그리기: name=선택항목, values='Survived'
    fig = 
    fig.update_traces
    fig.update_layout
    fig.update
    st.
with col2:
    # bar chart 그리기: x=선택 항목, y="Survived", color="Sex"
    fig = 
    fig.update_layout(height=400, width=400)
    st.

    
    
# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\6-3.chart.py