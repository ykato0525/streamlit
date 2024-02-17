import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px


# テキストデータに沿ってテーブルデータを抽出する
if 'data' in st.session_state:
    data = st.session_state['data']

fig = px.imshow(data)
st.plotly_chart(fig)


    