import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
from sklearn.cluster import KMeans
import plotly.figure_factory as ff


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

    elbow = px.line(x=ks, y=wcss)
    st.plotly_chart(elbow)

    n_clusters = st.selectbox(label="最適なクラスタ数を選択してください", options=ks)
    n_features = data.shape[0]
    # K-meansクラスタリングを適用
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(data)

    # データフレームを作成
    data['Cluster'] = clusters

    csv = data.to_csv()
    # Streamlitのダウンロードボタンを設定
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='dataframe.csv',
        mime='text/csv',
    )

    # clusterでソート
    data_sorted = data.sort_values('Cluster')


    fig = px.imshow(data_sorted.drop('Cluster', axis=1), aspect='auto')

    st.plotly_chart(fig)


else:
    st.write("データを入力してください")



    