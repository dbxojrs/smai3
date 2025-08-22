import streamlit as st
import time
from MyLLM import geminiTxt

# Sidebar
st.sidebar.markdown("Clicked Page 3")

# Page
st.title("Page3 프로그램 작성기")

text = st.text_area(label="질문입력:",placeholder="질문을 입력 하세요")
selected_option = st.radio("언어를 선택하세요", ["java", "python", "c++"])
st.write(f"선택된 옵션: {selected_option}")

if st.button("SEND"):
    if text:
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)

        prompt = f"'{text}'에 대해 설명해 줘. 선택한 언어: {selected_option}"
        result = geminiTxt(prompt)
        st.info(result)
    else:
        st.info("질문을 입력 하세요")


