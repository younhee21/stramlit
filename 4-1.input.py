# streamlit 라이브러리와 datetime 모듈 불러오기
import streamlit as st
from datetime import datetime  

st.title('Unit 4. Input Widgets')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/widgets')

st.header('1. Button')
if st.button('Say hello'):
    st.write('Hello')
else:
    st.write('Goodbye')


    

st.header('2. Radio button')
genre = st.radio('좋아하는 영화 장르를 선택하세요', ('코미디', 'SF', '액션'))
if genre == '코메디':
    st.write('코메디 유쾌하신 분이시군요')
elif genre == 'SF':
    st.write('저도 SF 좋아합니다')
else:  # 액션은 굳이 안써도 된다.
    st.write ('멋지십니다.') 




st.header('3. Checkbox')    # 😄
agree = st.checkbox ('I agree')
if agree:
    st.write('😄'*10)

    


st.header('4. Select box')
option = st.selectbox('어떻게 연락 드릴까요?', ('Email', 'Mobile phone', 'Office phone'))
st.write('네', option, '잘 알겠습니다')




st.header('5. Multi select')
options = st.multiselect ('좋아하는 색을 모두 선택하세요', ['Green', 'Yellow', 'Red', 'Blue'], ['Yellow', 'Red'])

st.write('선호 색상:', ', '.join(options))   # 선택된 색을 가로로 나타내는 방법

# st.write('선호 색상:')
# for i in options:
#    st.write (i)    # 이건 세로로 작성된다.




st.header('6. Input: Text/Number')
st.subheader('**_text_input_**')
title = st.text_input('최애 영화를 입력하세요', 'Sound of Music')  # 최초 입력 값
st.write ('당신이 가장 좋아하는 영화는 :', title)


st.subheader('**_number_input_**')
number = st.number_input('Insert a number(1 10)', min_value=1, max_value=10, value=5, step=1)  # min~max value:입력 허용구간, 최초 입력 값, 증분 값
st.write ('The current number is', number)




st.header('7. Date input')
ymd = st.date_input('When is your birthday', datetime(2000, 9, 6))   # 최초 입력 값, 근데 이렇게 하면 달력에 2010년까지만 나옴 => max_date를 지정해서 변경 가능 
st.write('Your birthday is:', ymd)
# max_date = datetime(2023, 10, 23) # 현재 날짜
# ymd = st.date_input('When is your birthday', datetime(2000, 9, 6), max_value=max_date) # 이렇게 하면 범위를 현재 날짜까지도 선택 가능함



st.header('8. Slider')
st.subheader('**_Slider- 이전 구간_**')
age = st.slider('나이가 어떻게 되세요?', 0, 130 , 25)  # 입력 허용구간(0~130), 최초 세팅 값(그래프상으로 0부터 25까지 선택됨)
st.write ('I am', age, 'years old')


st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
values = st.slider('값 구간을 선택하세요', 0.0, 100.0, (25.0, 75.0))   # (시작범위,끝범위, (첫해당구간,끝해당구간))
st.write ('Values:', values)


st.subheader('**_년 월 일 사이 구간_**')
slider_date = st.slider('날짜 구간을 선택하세요',
                        min_value=datetime(2022, 1, 1),
                        max_value=datetime(2022, 12, 31),  # min/max 생략 가능함
                        value=(datetime(2022, 6, 1), datetime(2022, 7, 31)), format=('YY/MM/DD'))
st.write ('slider date: ', slider_date)
st.write ('slider_date[0]:', slider_date[0], 'slider_date[1]:', slider_date[1])


# 년 월 일 시 사이 구간
# slider_time = st.slider(
#     'Select a range of datetime?',
#     datetime(2022, 1, 1, 0, 30), datetime(2022, 12, 31, 0, 30),
#     value=(datetime(2022, 7, 1, 0, 30), datetime(2022, 10, 31, 9, 30)),
#     format='MM/DD/YY - hh:mm')
# st.write('Slider time: ', slider_time)

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\4-1.input.py