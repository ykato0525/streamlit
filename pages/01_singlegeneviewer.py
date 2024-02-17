import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px

# テキストデータに沿ってテーブルデータを抽出する
if 'data' in st.session_state:
    data = st.session_state['data']

gene_list = data.index
print(gene_list)

# 遺伝子を選択するフォームを作成
gene = st.selectbox(label="遺伝子を選んでください", options=gene_list)
bar = go.Bar(
    x = data.columns,
    y = data.loc[gene, :]

)
fig = go.Figure(data=bar)
st.plotly_chart(fig)


# 棒グラフの描画
