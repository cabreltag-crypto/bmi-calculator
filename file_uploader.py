import pandas as pd
import numpy as np
import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns

st.title('FIle Uploader')
st.subheader('Import csv')
uploaded = st.file_uploader('choose a csv')
if uploaded:
    df = pd.read_csv(uploaded)
    st.subheader('Dataframe')
    st.write(df)
    cols1,cols2 = st.columns(2)
    with cols1:
        fig1 = plt.figure()
        sns.scatterplot(x='EstimatedSalary', y='Age',hue='Purchased',data=df)
        st.pyplot(fig1)
    with cols2:
        fig2=plt.figure()
        sns.histplot(x='Age',data=df)
        st.pyplot(fig2)
