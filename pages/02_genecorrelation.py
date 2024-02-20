import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# UIの表示
st.markdown("# 2つの遺伝子発現の相関を求める")

# テキストデータに沿ってテーブルデータを抽出する
if 'data' in st.session_state:
    data = st.session_state['data']



    gene_list_1 = data.index
    gene_list_2 = data.index


    # 遺伝子を選択するフォームを作成
    gene_1 = st.selectbox(label="x軸の遺伝子を選んでください", options=gene_list_1)

    # gene_1が決まったらすべての遺伝子との相関係数を算出して、上位５個を表示する

    ###########
    geneA = data.loc[gene_1]  # geneAを選択
    correlations = data.apply(lambda row: geneA.corr(row), axis=1)

    # 相関係数の絶対値を計算し、大きいものから順にソート
    sorted_correlations_1 = correlations.sort_values(ascending=False)
    sorted_correlations_2 = correlations.sort_values(ascending=True)
    # 上位10個の結果を表示

    st.markdown("選択した遺伝子との相関係数が大きい遺伝子のリスト(左: 正の相関; 右: 負の相関)")
    top_10 = sorted_correlations_1.head(10)
    low_10 = sorted_correlations_2.head(10)
    col1, col2 = st.columns(2)
    col1.write(top_10)
    col2.write(low_10)


    gene_2 = st.selectbox(label="y軸の遺伝子を選んでください", options=gene_list_2)

    x = data.loc[gene_1, :]
    y = data.loc[gene_2, :]

    pearson = np.corrcoef(x, y)
    st.write("peasonの相関係数: ", pearson[0, 1])

    fig = px.scatter(x=x, y=y,trendline='ols')
    st.plotly_chart(fig)
else:
    st.write("データを入力してください")


# 選択した遺伝子について簡単に検索できるようにする
gene_name = st.text_input("Enter the gene name:", "")
print(gene_name)

# 検索ボタン
if st.button('Search in GeneCards'):
    # GeneCardsのURLを構築
    url = f"https://www.genecards.org/cgi-bin/carddisp.pl?gene={gene_name}"
    
    # WebブラウザでURLを開く
    # リンクを表示
    st.markdown(f"[Search for {gene_name} in GeneCards]({url})", unsafe_allow_html=True)



