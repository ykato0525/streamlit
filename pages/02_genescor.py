import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import numpy as np


# テキストデータに沿ってテーブルデータを抽出する
if 'data' in st.session_state:
    data = st.session_state['data']

# UIの表示
st.markdown("# 2つの遺伝子発現の相関を求める")

gene_list_1 = data.index

gene_list_2 = data.index

# 遺伝子を選択するフォームを作成
gene_1 = st.selectbox(label="x軸の遺伝子を選んでください", options=gene_list_1)
gene_2 = st.selectbox(label="y軸の遺伝子を選んでください", options=gene_list_2)

x = data.loc[gene_1, :]
y = data.loc[gene_2, :]

pearson = np.corrcoef(x, y)
st.write("peasonの相関係数: ", pearson[0, 1])



fig = px.scatter(x=x, y=y,trendline='ols')
st.plotly_chart(fig)



