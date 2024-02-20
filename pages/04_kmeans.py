import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
from sklearn.cluster import KMeans


st.markdown("# KMeansで遺伝子を分類する")


# テキストデータに沿ってテーブルデータを抽出する
if 'data' in st.session_state:
    data = st.session_state['data']




    wcss = []

    for i in range(1, 21):
        clustering = KMeans(n_clusters=i, init='k-means++', random_state=20)
        clustering.fit(data)
        wcss.append(clustering.inertia_)
        
    ks = list(range(1, 21))

    fig = plt.plot(ks, wcss)
    st.pyplot(fig)

else:
    st.write("データを入力してください")



    