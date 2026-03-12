import streamlit as st
import time

# データ取得関数
@st.cache_data
def load_data():
    # データの取得や重い計算をシミュレート
    time.sleep(5)  # 5秒間待機
    return {"data": [1, 2, 3, 4, 5]}

# アプリケーションのタイトル
st.title("キャッシュ機能のデモ")

# データの読み込み
data = load_data()

# データの表示
st.write("取得したデータ:", data)