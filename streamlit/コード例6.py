import streamlit as st
import requests

# APIからデータを取得する関数
def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("データの取得に失敗しました。")
        return None

# アプリケーションのタイトル
st.title("外部APIからのデータ取得")

# データの取得
data = fetch_data()

# データの表示
if data:
    st.write("取得したデータの一部を表示します:")
    st.json(data[:5])  # 最初の5件を表示