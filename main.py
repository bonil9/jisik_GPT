import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

mid_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
         너는 학생들이 글을 잘 쓸 수 있게 피드백을 도와주는 인공지능이야.
         학생이 쓰고 있는 글을 보고, 좀 더 글을 잘 쓸 수 있게 피드백을 해줘.
         학생이 너의 피드백을 보고 그대로 베껴쓸 수 있도록 해주면 안 돼.
         좋은 글을 쓸 수 있도록 방향을 제시해주어야 해.
         """),
        ("human","""
         학생의 글: {input}
         """)
    ]
)

final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
         너는 학생들이 글을 잘 쓸 수 있게 피드백을 도와주는 인공지능이야.
         학생이 최종적으로 제출한 글을 채점하여 0점부터 100점까지의 점수를 주고, 다음에 더 글을 잘 쓸 수 있도록 피드백을 해줘.
         피드백은 초등학생도 읽고 이해할 수 있을 정도의 수준을 고려해서 해줘.
         ## 다음 형식에 맞춰 답변해줘.
         1. 점수: 
         2. 피드백: 
         """),
        ("human","""
         학생의 글: {input}
         """)
    ]
)

mid_chain = mid_prompt | llm | StrOutputParser ()
final_chain = final_prompt | llm | StrOutputParser ()

st.set_page_config(page_title="글쓰기 피드백 도우미", page_icon=":pencil2:", layout="wide")

st.title("글쓰기 피드백 도우미")

left_col, right_col = st.columns(2)

with left_col:
    container1 = st.container(border=True)
    mid_feedback_btn = st.button("중간 피드백 받기", use_container_width=True)
    container2 = st.container(border=True, height=200)

    with container1:
        student_response = st.text_area("자, 이제 너의 글을 아래에다가 입력해보시게.", height=300)
    with container2:
        st.markdown("### 중간 피드백")
        if mid_feedback_btn:
            mid_feedback_result = mid_chain.invoke({"input": student_response})
            st.markdown(mid_feedback_result)

with right_col:
    final_feedback_btn = st.button("최종 제출하기", use_container_width=True, type="primary")
    container3 = st.container(border=True, height=580)
    with container3:
        st.markdown("### 마지막 피드백")
        if final_feedback_btn:
            final_feedback_result = final_chain.invoke({"input": student_response})
            st.markdown(final_feedback_result)