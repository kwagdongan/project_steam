import streamlit as st
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

st.title("Steam 게임 태그 분석")

uploaded_file = st.file_uploader(
    "dataset.csv",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if "tags" not in df.columns:
        st.error("'tags' 컬럼이 존재하지 않습니다.")
    else:
        # 태그 분리 및 카운트
        tag_counter = Counter()

        for tags in df["tags"].dropna():
            tag_list = [tag.strip() for tag in str(tags).split("|")]
            tag_counter.update(tag_list)

        # 데이터프레임 생성
        tag_df = pd.DataFrame(
            tag_counter.items(),
            columns=["Tag", "Count"]
        ).sort_values(
            by="Count",
            ascending=False
        )

        st.subheader("태그 빈도 순위")
        st.dataframe(tag_df)

        # Top 20 시각화
        top_n = 20
        top_tags = tag_df.head(top_n)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(
            top_tags["Tag"][::-1],
            top_tags["Count"][::-1]
        )

        ax.set_title(f"Top {top_n} Tags")
        ax.set_xlabel("Count")

        st.pyplot(fig)
