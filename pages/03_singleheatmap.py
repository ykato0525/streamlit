import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px




# テキストデータに沿ってテーブルデータを抽出する
if 'data' in st.session_state:
    data = st.session_state['data']

st.markdown("# 複数遺伝子の発現を閲覧する")

demo_sets = ["geneA", "geneB", "geneC"]

gene_list = ["all", 
             "demo"]

# データセットを選択できるようにする
geneset = st.selectbox(label="閲覧したいデータセットを選択してください", options=gene_list)

# データセットを抽出する
if geneset == "demo":
    data = data.loc[demo_sets]

fig = px.imshow(data)
st.plotly_chart(fig)

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

    