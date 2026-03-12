#見出し
import streamlit as st
import pandas as pd

# サンプルデータの作成
data = {
    '名前': ['Alice', 'Bob', 'Charlie', 'David'],
    '年齢': [24, 27, 22, 32],
    '職業': ['エンジニア', 'デザイナー', 'ライター', 'マネージャー']
}

df = pd.DataFrame(data)

# アプリケーションのタイトル
st.title("データの表示方法を学ぼう")

# st.tableを使ったデータの表示
st.header("st.tableを使った静的なテーブル表示")
st.table(df)

# st.dataframeを使ったデータの表示
st.header("st.dataframeを使ったインタラクティブなデータフレーム表示")
st.dataframe(df)