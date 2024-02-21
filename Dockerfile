# Use the official Python base image
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# Install the required packages
RUN pip install streamlit==1.31.0
RUN pip install pandas
RUN pip install plotly
RUN pip install seaborn
RUN pip install statsmodels
RUN pip install jupyter notebook
RUN pip install scipy
RUN pip install scikit-learn
RUN pip install scanpy
RUN pip install jupyterlab

COPY . ./


# Expose the default Streamlit & jupyter port
EXPOSE 8501

# Streamlitアプリケーションを実行
CMD streamlit run RNAseqanalyzer.py



