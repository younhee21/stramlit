import streamlit as st
import pandas as pd
from datetime import datetime  

st.header('날짜 구간으로 데이터 조회하기')

# streamlit\data_subway_in_seoul.csv  
# 한글 encoding='cp949' 추가하여 읽어오고 확인하기 
# cp949(마이크로소프트용 한글체계), utf8(모든 브라우저에서 사용가능한 한글체계)
df = pd.read_csv('streamlit\data_subway_in_seoul.csv', encoding='cp949')

# 날짜 필드의 데이터 형식 확인하기
st.write('날짜 필드 형식:', df['날짜'].dtypes)

# 데이터프레임 내용 확인하기
st.write(df)




# 날짜 컬럼을 string에서 datetime으로 변환하기
df['날짜'] = pd.to_datetime(df['날짜'], format='%Y-%m-%d')

# 날짜 필드의 데이터 형식 확인하기
st.write('날짜 필드 형식:', df['날짜'].dtypes)

# 데이터프레임 내용 확인하기
st.write(df)




# slider를 사용하여 날짜 구간 설정하기
slider_date = st.slider('날짜 구간을 선택하세요',
                        datetime(2021, 1, 1), datetime(2021, 12, 31),           # 날짜 전체 구간 : 2021.1.1~2021.12.31
                        value= (datetime(2021, 7, 1), datetime(2021, 7, 31)),    # 초기 설정 구간 : 2021.7.1~2021.7.31
                        format=('YY/MM/DD'))                                    # 날짜 형식: YY/MM/DD

# slider_date의 구간 날짜 확인하기
st.write ('slider_date[0]:', slider_date[0], 'slider_date[1]:', slider_date[1])

# slider_date의 선택된 시작, 종료 날짜를 start_date, end_date에 저장하기
start_date = slider_date[0]
end_date = slider_date[1]

# slider 날짜 구간으로 df를 읽어서 새 sel_df 으로 저장하고 확인하기
sel_df = df.loc[df['날짜'].between(start_date, end_date)]
st.dataframe(sel_df)


# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\4-2.input.py