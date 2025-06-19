import streamlit as st

con1 = st.container(border=True)

con2 = st.container(border=True)

with con1:
    st.markdown("### 첫번째 컨테이너입니다!")

with con2:
    st.markdown("### 두번째 컨테이너입니다!")
