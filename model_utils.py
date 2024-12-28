import pickle
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Load model dari file model_svm.pkl
def load_model(model_path='./model/best_rf_model.pkl'):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# # Fungsi untuk menyimpan data input dan hasil prediksi ke file CSV
# def save_input_and_prediction_to_csv(data, prediction, filename='./data/inputs_predictions.csv'):
#     # Tambahkan kolom hasil prediksi ke DataFrame
#     data['Prediction'] = prediction

#     # Periksa apakah file sudah ada
#     if not os.path.isfile(filename):
#         # Jika belum, buat file baru dengan header
#         data.to_csv(filename, index=False)
#     else:
#         # Jika sudah ada, tambahkan data tanpa menimpa header
#         data.to_csv(filename, mode='a', header=False, index=False)



# Fungsi untuk menyimpan data input dan hasil prediksi ke Google Drive
def save_input_and_prediction_to_google_drive(data, prediction, filename='inputs_predictions.csv'):
    # Tambahkan kolom hasil prediksi ke DataFrame
    data['Prediction'] = prediction

    # Simpan file CSV lokal sementara
    data.to_csv(filename, index=False)

    # Autentikasi Google Drive
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    # Unggah file ke Google Drive
    file_drive = drive.CreateFile({'title': filename})
    file_drive.SetContentFile(filename)
    file_drive.Upload()
    print(f"File {filename} uploaded to Google Drive!")


# Prediksi menggunakan model
def make_prediction(model, input_data):
    return model.predict(input_data)
