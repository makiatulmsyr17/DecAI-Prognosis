import pickle
import os

# Load model dari file model_svm.pkl
def load_model(model_path='./model/best_rf_model.pkl'):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

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

# Prediksi menggunakan model
def make_prediction(model, input_data):
    return model.predict(input_data)

