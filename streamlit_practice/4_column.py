import streamlit as st

st.markdown("# 컬럼 레이아웃 예제")

col1, col2 = st.columns(2)

with col1:
    container1 = st.container(border=True)
    with container1:
        st.markdown("## 첫번째 컬럼 컨테이너")
    st.markdown("### 첫번째 컬럼입니다!")
    st.markdown("여기는 첫번째 컬럼의 내용입니다.")

with col2:
    st.markdown("### 두번째 컬럼입니다!")
    st.markdown("여기는 두번째 컬럼의 내용입니다.")