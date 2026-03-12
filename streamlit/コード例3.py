import streamlit as st
import pandas as pd

# ファイルアップロードウィジェットの作成
uploaded_file = st.file_uploader("ファイルをアップロードしてください", type=["csv", "txt"])

# ファイルがアップロードされた場合の処理
if uploaded_file is not None:
    # CSVファイルをデータフレームとして読み込む
    df = pd.read_csv(uploaded_file)
    st.write("アップロードされたファイルの内容:")
    st.dataframe(df)