import pickle
import streamlit as st

model = pickle.load(open('estimasi_kolesterol.sav', 'rb'))

st.title('Estimasi Jumlah Kandungan Kolesterol dalam Makanan')

Carbohydrt = st.number_input('Input jumlah Karbohidrat (g)')
Calcium  = st.number_input('Input jumlah kalsium (mg)')
Water_g = st.number_input('Input jumlah Air (g)')
Sodium  = st.number_input('Input jumlah Sodium (mg)')
Zinc  = st.number_input('Input jumlah Zinc')

predict = ''

if st.button('Estimasi'):
    predict = model.predict(
        [[Carbohydrt, Calcium, Water_g, Sodium, Zinc]]
    )
    st.write ('Estimasi Kandungan Kolesterol dalam Makanan (mg): ', predict)