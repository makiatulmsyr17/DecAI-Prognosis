import pickle
import streamlit as st
import pandas as pd
import os

# Load model dari file model_svm.pkl
with open('./model/best_rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Aplikasi Streamlit
st.title('DecAI Prognosis: Predicting the 10-Year Risk of Mortality')

# CSS untuk membuat desain hitam putih dan tombol hitam
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #000000;
        color: #FFFFFF;
        border-radius: 5px;
        border: 1px solid #FFFFFF;
    }
    .stButton>button:hover {
        background-color: #333333;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Fungsi untuk reset input
def reset_input():
    st.session_state['Age'] = 0.0
    st.session_state['Pulse pressure'] = 0.0
    st.session_state['Systolic BP'] = 0.0
    st.session_state['Diastolic BP'] = 0.0
    st.session_state['Serum Cholesterol'] = 0.0
    st.session_state['Sedimentation rate'] = 0.0
    st.session_state['Sex'] = 0.0
    st.session_state['Serum Albumin'] = 0.0

# Tombol Reset ditekan
if 'reset' not in st.session_state:
    st.session_state['reset'] = False

if st.button('Reset'):
    reset_input()
    st.session_state['reset'] = True

# Input dari pengguna sesuai urutan yang benar
Age = st.number_input('Masukkan nilai untuk Age:', value=st.session_state.get('Age', 0.0), key='Age')
Pulse_pressure = st.number_input('Masukkan nilai untuk Pulse pressure:', value=st.session_state.get('Pulse pressure', 0.0), key='Pulse pressure')
Systolic_BP = st.number_input('Masukkan nilai untuk Systolic_BP:', value=st.session_state.get('Systolic BP', 0.0), key='Systolic BP')
Diastolic_BP = st.number_input('Masukkan nilai untuk Diastolic BP:', value=st.session_state.get('Diastolic BP', 0.0), key='Diastolic BP')
Serum_Cholesterol = st.number_input('Masukkan nilai untuk Serum Cholesterol:', value=st.session_state.get('Serum Cholesterol', 0.0), key='Serum Cholesterol')
Sedimentation_rate = st.number_input('Masukkan nilai untuk Sedimentation rate:', value=st.session_state.get('Sedimentation rate', 0.0), key='Sedimentation rate')
Sex = st.number_input('Masukkan nilai untuk Sex:', value=st.session_state.get('Sex', 0.0), key='Sex')
Serum_Albumin = st.number_input('Masukkan nilai untuk Serum Albumin:', value=st.session_state.get('Serum Albumin', 0.0), key='Serum Albumin')


# Fungsi untuk menyimpan data input dan hasil prediksi ke file CSV
def save_input_and_prediction_to_csv(data, prediction, filename='./data/inputs_predictions.csv'):
    # Tambahkan kolom hasil prediksi ke DataFrame
    data['Prediction'] = prediction

    # Periksa apakah file sudah ada
    if not os.path.isfile(filename):
        # Jika belum, buat file baru dengan header
        data.to_csv(filename, index=False)
    else:
        # Jika sudah ada, tambahkan data tanpa menimpa header
        data.to_csv(filename, mode='a', header=False, index=False)

# Tombol Predict
if st.button('Predict'):
    # Buat DataFrame dari input pengguna sesuai dengan urutan fitur saat pelatihan
    input_data = pd.DataFrame({
        'Age': [Age],
        'Pulse pressure': [Pulse_pressure],
        'Systolic BP': [Systolic_BP],
        'Diastolic BP': [Diastolic_BP],
        'Serum Cholesterol': [Serum_Cholesterol],
        'Sedimentation rate': [Sedimentation_rate],
        'Sex': [Sex],
        'Serum Albumin': [Serum_Albumin],
    })

    # Prediksi menggunakan model yang sudah diload
    prediction = model.predict(input_data)
    
    # Simpan data input dan hasil prediksi ke file CSV
    save_input_and_prediction_to_csv(input_data, prediction)

    # Tampilkan hasil prediksi
    if prediction[0] == 1.0:
        st.write('Hasil Prediksi: **Beresiko Kematian** 10 tahun kedepan')
    elif prediction[0] == 0.0:
        st.write('Hasil Prediksi: **Tidak Beresiko Kematian**')
    else:
        st.write('Hasil Prediksi: Nilai prediksi tidak valid.')
