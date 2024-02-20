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

if uploaded_tpm_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_tpm_file, index_col=0)
    st.write(dataframe)
    st.session_state['data'] = dataframe

st.markdown("ここに入れるcsvファイルには遺伝子が縦、細胞が横に入るように整形してください")

st.markdown("### step2: singlegeneviewer / genecorrelation / singleheatmap に進む")
st.markdown("サイドバーのアプリ名をクリックすると解析に進めます。")
st.markdown("###  singlegeneviewer")
st.markdown("遺伝子名を選択すると各サンプルでの発現量が棒グラフで閲覧できます。")
st.markdown("###  genecorrelation")
st.markdown("遺伝子名を選択すると各サンプルでの発現量が散布図で表示されます。この解析では相関係数も算出します。")
st.markdown("###  singleheatmap")
st.markdown("すべてのサンプルのすべての遺伝子の発現をヒートマップで閲覧できます")

st.markdown("## パート2: ちょっと高度な解析")
st.markdown("パート2は現在実装中です")
st.markdown("### step1:以下のフォームにテキストファイルをドラッグ&ドロップしてください")
st.markdown("必要なファイルは、count値のデータとメタデータです")

# countファイルの入力
uploaded_count_file = st.file_uploader("Choose a count file", type="csv")

if uploaded_count_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    count_data = pd.read_csv(uploaded_count_file, index_col=0)
    st.write(count_data)
    st.session_state['count_data'] = count_data


# metadataの入力
uploaded_meta_file = st.file_uploader("Choose a metadata file", type="csv")

if uploaded_meta_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    meta_data = pd.read_csv(uploaded_meta_file, index_col=0)
    st.write(meta_data)
    st.session_state['metadata'] = meta_data

st.markdown("### step2:サイドバーの extractdegs / enrichmentanalysis / clustermap に進んでください。")