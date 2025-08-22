import streamlit as st
import time
from MyLLM import geminiTxt

# Sidebar
st.sidebar.markdown("Clicked Page 5")

# Page
st.title("Page5")

import face_recognition
import cv2

# 웹캠 열기
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # 얼굴 위치 찾기
    face_locations = face_recognition.face_locations(frame)

    # 얼굴에 사각형 그리기
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # 화면에 출력
    cv2.imshow('Video', frame)

    # q 키 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
