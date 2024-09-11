import streamlit as st

from web_functions import predict

def app(df, x, y):

    st.title("Prediction Page")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Input Nilai Age')
    with col1:    
        ureum = st.text_input('Input Nilai Ureum')
    with col1:    
        creatinin = st.text_input('Input Nilai Kreatinin')
    
    features = [age,ureum,creatinin]

    # Tombol Prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x,y,features)
        score = score
        st.info("Prediksi Sukses...")
        
        if (prediction == 1):
            st.warning("Orang Tersebut Rentan Terkena Penyakit Ginjal")
        else:
            st.success("Orang Tersebut Relatif Aman dari Penyakit Ginjal")

        st.write("Model yang Digunakan Memiliki Tingkat Akurasi", (score*100),"%")
        
    