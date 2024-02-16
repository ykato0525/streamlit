import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px



uploaded_file = st.file_uploader("Choose a file", type="csv")
df = pd.read_csv(uploaded_file, index_col=0)



if uploaded_file is not None:
    st.write(df)

fig = px.imshow(df)
fig.update_layout(width=600, height=1000)  
st.plotly_chart(fig)

# テキストデータに沿ってテーブルデータを抽出する