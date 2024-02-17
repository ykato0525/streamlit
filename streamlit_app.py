import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px


st.markdown("# このアプリの使い方")
st.markdown("### 以下のフォームにcsvファイルをドラッグ&ドロップしてください")

uploaded_file = st.file_uploader("Choose a file", type="csv")

if uploaded_file is not None:

    # Can be used wherever a 