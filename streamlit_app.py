import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px


st.markdown("# このアプリの使い方")
st.markdown("## singleheatmap")
st.markdown("細胞名と遺伝子発現データが記載されたcsvファイルをドラッグアンドドロップするとheatmapが自動で描画されます")