import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader("複数のファイルをアップロードしてください", type=["csv"], accept_multiple_files=True)

if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        st.write(f"{uploaded_file.name}の内容:")
        st.dataframe(df)