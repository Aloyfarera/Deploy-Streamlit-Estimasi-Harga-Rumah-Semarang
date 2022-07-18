import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pickle
import plotly.express as px



st.set_page_config(page_title='Estimasi Harga rumah Semarang', page_icon='house')

df = pd.read_csv("rumahsmg.csv")
df = df.drop(['Unnamed: 0'] ,axis  = 1)

st.write("""
### Estimasi Harga Rumah Anda Secara Gratis.
Estimasi Dari Harga adalah berdasarkan informasi yang anda masukan.
""")
st.write("""
Dataset ini adalah hasil scraping dari website rumah123.com
Kususnya di kota Semarang Jawa Tengah.
""")
st.subheader('Parameter yang anda masukan')
st.sidebar.header('Masukan Parameter Untuk Mengestimasikan Harga Rumah Anda')
kode_pos=[5021,234]

#def user_input_features():
option = ('banyumanik','candisari','gajah mungkur','gayamsari','genuk',
'gunung pati','mijen','ngaliyan', 'pedurungan','semarang barat','semarang selatan','semarang tengah','semarang timur','semarang utara','tembalang','tugu')
option2 =("no","yes")
kecamatan = st.sidebar.selectbox('Pilih Kecamatan',['banyumanik','candisari','gajah mungkur','gayamsari','genuk',
'gunung pati','mijen','ngaliyan', 'pedurungan','semarang barat','semarang selatan','semarang tengah','semarang timur','semarang utara','tembalang','tugu'])
#kecamatan = st.sidebar.selectbox("Masukan Lokasi", range(len(option)), format_func=lambda x: option[x])
if   kecamatan == "tembalang":
     kecamatan = 14
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50271,max_value=50279,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.414270,110.475850)
     latitude = st.sidebar.slider('Masukan latitude',-7.065130,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',3.479345,13.474958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari Bandara Ahmad Yani',3.462800,13.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',4.962800,13.420384)
elif kecamatan == 'banyumanik':
     kecamatan = 0
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50261,max_value=50269,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.428650,110.446131)
     latitude = st.sidebar.slider('Masukan latitude',-7.086245,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',4.825997,13.474958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',6.995981,13.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',4.962800,13.420384)
elif kecamatan == "pedurungan":
     kecamatan = 8
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50191,max_value=50199,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.465850,110.475850)
     latitude = st.sidebar.slider('Masukan latitude',-7.008900,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',1.104285,6.610483)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',10.474958,13.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',1.162800,6.420384)
elif kecamatan == "gajah mungkur":
     kecamatan = 2
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50231,max_value=50237,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.406240,110.414480)
     latitude = st.sidebar.slider('Masukan latitude',-7.004469,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',2.262091,13.474958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',3.462800,13.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',2.262800,13.420384)
elif kecamatan == "ngaliyan":
     kecamatan = 7
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50181,max_value=50189,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.301580,	110.475850)
     latitude = st.sidebar.slider('Masukan latitude',-7.063034,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',4.327022,13.736553)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',3.462800,13.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',4.262800,13.420384)
elif kecamatan == "gayamsari":
     kecamatan = 3
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50151,max_value=50167,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.301580,110.455538)
     latitude = st.sidebar.slider('Masukan latitude',-7.001198,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',2.399137,7.449866)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',3.462800,13.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',2.562800,8.420384)
elif kecamatan == "genuk":
     kecamatan = 4
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50111,max_value=50118,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.469768,110.475850)
     latitude = st.sidebar.slider('Masukan latitude',-6.975149,-6.963677)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',5.948461,7.660848)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',10.224076,12.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',5.962800,9.420384)
elif kecamatan == "gunung pati":
     kecamatan = 5
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50221,max_value=50229,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.358262,110.396929)
     latitude = st.sidebar.slider('Masukan latitude',-7.086245,-7.022686)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',4.601784,12.474958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',3.462800,12.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',4.662800,12.420384)
elif kecamatan == 'candisari':
     kecamatan = 1
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50251,max_value=50257,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.301580,110.438429)
     latitude = st.sidebar.slider('Masukan latitude',-7.026560,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',2.479345,0.674958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',12.462800,9.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',1.962800,13.420384)
elif kecamatan == "mijen":
     kecamatan = 6
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50211,max_value=50219,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.313364,110.385991)
     latitude = st.sidebar.slider('Masukan latitude',-7.049416,-6.978920)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',3.479345,13.474958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',3.462800,13.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',3.962800,13.420384)
elif kecamatan == "tugu":
     kecamatan = 15
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50151,max_value=50156,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.344652,110.348754)
     latitude = st.sidebar.slider('Masukan latitude',-6.973593,-6.971876)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',8.479345,3.474958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',8.462800,3.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',6.962800,13.420384)
elif kecamatan == "semarang tengah":
     kecamatan = 11
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50131,max_value=50139,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.301580,110.459941)
     latitude = st.sidebar.slider('Masukan latitude',-7.015050,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',0.879345,3.474958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',1.462800,4.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',0.762800,5.420384)
elif kecamatan == "semarang barat":
     kecamatan = 9
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50141,max_value=50149,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.301580,110.412666)
     latitude = st.sidebar.slider('Masukan latitude',-7.011184,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',1.479345,4.674958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',0.462800,3.20384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',0.262800,5.420384)
elif kecamatan == "semarang utara":
     kecamatan = 13
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50171,max_value=50179,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.387031,110.417864)
     latitude = st.sidebar.slider('Masukan latitude',-6.973830,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',2.079345,8.474958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',1.462800,5.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',1.962800,7.420384)
elif kecamatan == "semarang selatan":
     kecamatan = 10
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50241,max_value=50249,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.301580,110.475850)
     latitude = st.sidebar.slider('Masukan latitude',-7.057671,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',0.879345,13.474958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',4.6462800,13.420384)
elif kecamatan == "semarang timur":
     kecamatan = 12
     kode_pos = st.sidebar.number_input('Masukan Kode Pos',min_value =50122,max_value=50128,step=1)
     longitude = st.sidebar.slider('Masukan longitude',110.301580,110.475850)
     latitude = st.sidebar.slider('Masukan latitude',-7.034369,-6.954490)
     jarak_simpanglima = st.sidebar.slider('Masukan Jarak dari Simpang Lima',1.379345,5.474958)
     jarak_bandara = st.sidebar.slider('Masukan Jarak dari bandara Ahmad Yani',3.462800,8.420384)
     jarak_stasiun = st.sidebar.slider('Masukan Jarak dari Stasiun Poncol',1.962800,8.420384)
     
kamar_tidur= st.sidebar.number_input('Masukan Jumlah Kamar Tidur',min_value=1,max_value=10,value=3,step=1)
kamar_mandi = st.sidebar.number_input('Masukan Jumlah Kamar Mandi',min_value=1,max_value=10,value=3,step=1)
luas_bangunan= st.sidebar.number_input('Masukan Luas Bangunan per m2',min_value=0,max_value=1200,value=200)
luas_tanah = st.sidebar.number_input('Masukan Luas Tanah  per m2',min_value=0,max_value=1200,value=200)
garasi = st.sidebar.number_input('Masukan Jumlah Garasi',min_value=0,max_value=4,value=1)
jumlah_lantai= st.sidebar.number_input('Masukan Jumlah Lantai Rumah',min_value=1,max_value=10,value=1,step=1)
carport= st.sidebar.selectbox("Carport",range(len(option2)), format_func=lambda x: option2[x])
taman = st.sidebar.selectbox("Taman",range(len(option2)), format_func=lambda x: option2[x])
keamanan24jam = st.sidebar.selectbox("keamanan 24 jam",range(len(option2)), format_func=lambda x: option2[x])
pagar = st.sidebar.selectbox("Pagar",range(len(option2)), format_func=lambda x: option2[x])



data = { 'kamar tidur':kamar_tidur,
    'kamar mandi':kamar_mandi,
    'luas_bangunan':luas_bangunan,
    'luas_tanah':luas_tanah,
    'Garasi':garasi,
    'Taman':taman,
    'keamanan 24 jam':keamanan24jam,
    'carport':carport,
    'lokasi':kecamatan,
    'longitude':longitude,
    'latitude':latitude,
    'kode_pos':kode_pos,
    'jumlah_lantai':jumlah_lantai,
    'pagar':pagar,
    'jarak_simpanglima':jarak_simpanglima,
    'jarak_bandara':jarak_bandara,
    'jarak_stasiun':jarak_stasiun}
features = pd.DataFrame(data,index=[0])

latlong = features[['latitude','longitude']]
st.map(latlong)


  #return features

inp_df = features

st.write(inp_df)
def run():
    model = pickle.load(open('model_estimasi.sav', 'rb'))
    harga = model.predict(inp_df)
    st.subheader('Harga Rumah')
    st.subheader("Estimasi Harga Rumah Anda Rp " + str('%.0f' % np.expm1(harga)))
    

btn = st.sidebar.button("Estimasi Sekarang")
if btn:
	run()
else:
	pass
   


