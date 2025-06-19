import streamlit as st

st.markdown("# 자기소개 페이지")

btn1 = st.button("자기소개 버튼")

if btn1:
    st.markdown("안녕하세요! 저는 구본일입니다.")
    st.markdown("버튼을 클릭해보세요!")
    st.markdown("버튼을 클릭하면 자기소개가 나타납니다.")