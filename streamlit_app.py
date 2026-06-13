import streamlit as st
import pandas as pd

import os
# 현재 경로에 pages 폴더가 있는지 확인
st.write(f"현재 경로: {os.getcwd()}")
st.write(f"pages 폴더 존재 여부: {os.path.exists('pages')}")

st.set_page_config(page_title="Steam 분석 앱", layout="wide")

st.title("🎮 Steam 게임 태그 분석 대시보드")
st.write("왼쪽 사이드바에서 분석 페이지를 선택하세요.")
# 사이드바에 글자 하나만 띄워보기
st.sidebar.title("테스트 사이드바")
@st.cache_data
def load_data():
    return pd.read_csv("datas.csv")

df = load_data()
st.metric("전체 데이터 개수", f"{df.shape[0]:,} 개")
