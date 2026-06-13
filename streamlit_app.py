import streamlit as st
import pandas as pd

st.set_page_config(page_title="Steam 분석", layout="wide")

st.title("제목 테스트 중")
st.write("사이드바")

try:
    @st.cache_data
    def load_data():
        return pd.read_csv("datas.csv", encoding='utf-8')
    
    df = load_data()
    st.metric("전체 데이터 개수", f"{df.shape[0]:,} 개")
except Exception as e:
    st.error(f"데이터 로드 실패: {e}")
