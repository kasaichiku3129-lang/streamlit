import streamlit as st

st.title("ゆかいななかまたち")

st.header("児島家")

st.subheader("メンバー紹介です")

st.write("こんにちは、児島家へようこそ")

st.write("数値も表示できます:",123)

import pandas as pd
df = pd.DataFrame({'名前':["taka", "hiro", "saku", "kai"], '年齢': [37, 37, 6, 1]})
st.write("データフレームの表示",df)
