import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px


st.markdown("# このアプリの使い方")
st.markdown("このページでは遺伝子発現のカウント値算出後の解析を行います")
st.markdown("## パート1:遺伝子発現を可視化する")
st.markdown("### step1:以下のフォームにcsvファイルをドラッグ&ドロップしてください")
st.markdown("データの入力がない状態だと各解析ページになにも出ません。")
st.markdown("最初の入力がTPM値または、log2(TPM)値であることを想定しています。")


uploaded_tpm_file = st.file_uploader("Choose a tpm file", type="csv")
is_t = st.radio("", ("転置しない", "転置する"), horizontal=True)

if uploaded_tpm_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_tpm_file, index_col=0)
    if is_t == "転置する":
        dataframe = dataframe.T
    st.write(dataframe)
    st.session_state['data'] = dataframe

st.markdown("ここに入れるcsvファイルには遺伝子が縦、細胞が横に入るように整形してください")

# metadataの入力
uploaded_meta_file = st.file_uploader("Choose a metadata file", type="csv")

if uploaded_meta_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    meta_data = pd.read_csv(uploaded_meta_file, index_col=0)
    st.write(meta_data)
    st.session_state['metadata'] = meta_data

st.markdown("### step2: singlegeneviewer / genecorrelation / singleheatmap に進む")
st.markdown("サイドバーのアプリ名をクリックすると解析に進めます。")
st.markdown("###  singlegeneviewer")
st.markdown("遺伝子名を選択すると各サンプルでの発現量が棒グラフで閲覧できます。")
st.markdown("###  genecorrelation")
st.markdown("遺伝子名を選択すると各サンプルでの発現量が散布図で表示されます。この解析では相関係数も算出します。")
st.markdown("###  singleheatmap")
st.markdown("指定した遺伝子群の発現をヒートマップで閲覧できます")
st.markdown("###  KMeans")
st.markdown("KMeansでクラスタリングして遺伝子を分類します")