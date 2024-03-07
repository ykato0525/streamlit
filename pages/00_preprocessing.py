import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px

st.markdown("# データの前処理")

st.markdown("## サンプル情報（metadata)を入力してください")
# metadataの入力
uploaded_meta_file = st.file_uploader("Choose a metadata file", type="csv")

if uploaded_meta_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    meta_data = pd.read_csv(uploaded_meta_file, index_col=0)
    st.write(meta_data)
    st.session_state['metadata'] = meta_data

st.markdown("サンプル情報は以下のように記載してください")