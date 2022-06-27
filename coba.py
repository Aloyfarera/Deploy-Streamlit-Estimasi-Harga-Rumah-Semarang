# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 01:50:29 2022

@author: ASUS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pickle



st.set_page_config(page_title='Estimasi Harga rumah Semarang', page_icon='house')

df = pd.read_csv("rumahku.csv")
df = df.drop(['Unnamed: 0','Unnamed: 0.1'] ,axis  = 1)

st.write("""
### Estimasi Harga Rumah Anda Secara Gratis.
Valuations are estimates based on information that you provide.
""")
st.write("""
This dataset is the result of scraping from rumah.com website, especially in the city of Semarang .
""")

st.write("""
In this project we are going to use random forest to estimate the price.
It's very easy to do, and you can check the code by clicking on button below.
""")

st.write("""
#### You can find this project on GitHub.
[[Model Building](https://github.com/p4v10/Housing-Price-Predicting)]
[[Model Deployment](https://github.com/p4v10/Heart_Disease_Streamlit)]
""")
'''
st.write("""
#### You can find this project on GitHub.
[[Model Building](https://github.com/p4v10/Housing-Price-Predicting)]
[[Model Deployment](https://github.com/p4v10/Heart_Disease_Streamlit)]
""")
'''

selector = st.selectbox('Pilih Chart Yang Anda Butuhkan',('Persebaran Harga','Jumlah kamar tidur','Jumlah kamar mandi','Jumlah Kecamatan','Luas Tanah Harga','Luas Bangunan Harga','Korelasi Antar Variabel'))
if selector == 'Persebaran Harga':
    price_graph = plt.figure(figsize=(10,6))
    sns.distplot(df['harga'],color='crimson')
    st.pyplot(price_graph)

if selector == 'Jumlah kamar tidur':
    br_graph = plt.figure(figsize=(10,6))
    sns.countplot(x="kamar_tidur", data=df,order = df['kamar_tidur'].value_counts().index)
    st.pyplot(br_graph)

if selector == 'Jumlah kamar mandi':
    kamar_mandi_graph = plt.figure(figsize=(10,6))
    sns.countplot(x="kamar_mandi", data=df,order = df['kamar_mandi'].value_counts().index)
    st.pyplot(kamar_mandi_graph)


if selector == 'Jumlah Kecamatan':
    kecamatan_graph = plt.figure(figsize=(10,6))
    sns.countplot(y="kecamatan", data=df,order = df['kecamatan'].value_counts().index)
    st.pyplot(kecamatan_graph)

if selector == 'Luas Tanah Harga':
    lt_graph = plt.figure(figsize=(10,6))
    sns.scatterplot(x="luas_tanah",y="harga",hue="kecamatan",data=df)
    st.pyplot(lt_graph)
if selector == 'Luas Bangunan Harga':
    lb_graph = plt.figure(figsize=(10,6))
    sns.scatterplot(x="luas_bangunan",y="harga",hue="kecamatan",data=df)
    st.pyplot(lb_graph)
if selector == 'Korelasi Antar Variabel':
    cor_graph = plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(),annot=True)
    st.pyplot(cor_graph)


non_top_1_perc = df.sort_values('harga', ascending=False).iloc[216:]




st.subheader('Parameters that you provided')
st.sidebar.header('Masukan Parameter Untuk Mengestimasikan Harga Rumah Anda')

app_mode = st.sidebar.selectbox('Select Page',['Home','Estimasi'])

option = ('banyumanik','candisari','gajah mungkur','gayamsari','genuk',
  'gunung pati','mijen','ngaliyan', 'pedurungan','semarang barat','semarang selatan','semarang tengah','semarang timur','semarang utara','tembalang','tugu')
option2 =("no","yes")
kecamatan = st.sidebar.selectbox("Masukan Lokasi", range(len(option)), format_func=lambda x: option[x])
if   kecamatan == 1:
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50271,max_value=50279,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "banyumanik":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50261,max_value=50269,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "pedurungan":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50191,max_value=50199,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "gajah mungkur":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50231,max_value=50237,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "ngaliyan":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50181,max_value=50189,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "gayamsari":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50151,max_value=50167,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "genuk":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50111,max_value=50118,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "gunung pati":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50221,max_value=50229,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "candisari":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50251,max_value=50257,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "mijen":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50211,max_value=50219,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "tugu":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50151,max_value=50156,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "semarang tengah":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50131,max_value=50139,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "semarang barat":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50141,max_value=50149,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "semarang utara":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50171,max_value=50179,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "semarang selatan":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50241,max_value=50249,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)
elif kecamatan == "semarang timur":
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50122,max_value=50128,value=3,step=1)
     longitude = st.sidebar.slider('Masukan longitude',0,10000,0,)
     latitude = st.sidebar.slider('Masukan latitude',0,10000,0,)