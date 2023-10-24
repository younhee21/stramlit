# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

# header, subheader, text, caption 연습하기
st.title('Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')





# markdown 연습하기
st.markdown('# Markdown 1st')
st.markdown('## Markdown 2nd')
st.markdown('### Markdown 3rd')
st.markdown('**_Markdown 진하고 기울임_**')
st.markdown('- Markdown 글머리 기호')



# Latex & Code 연습하기
st.markdown('## 3. Code & Latex')
st.code('x=1234')
st.code('a + ar + ar^2 + ar^3')
st.latex(r''' a + ar + ar^2 + ar^3 + \cdots + ar^{n-1} = \sum_{k=0}^{n-1}ar^k = a \left(\frac{1-r^{n}}{1-r}\right) ''')
st.latex(r''' a + ar + ar^2 + ar^3 ''')



# write 연습하기
st.title('write')
st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')
st.write ('this is a string')
st.write ('Hello, *World!* 😄')

st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')
st.caption("{'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']}")
df = pd.DataFrame({'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']})
st.write('딕셔너리를 판다스의 데이터 프레임으로 바꿔서', df, '스트림릿의 write함수로 표현')


# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\1.text.py