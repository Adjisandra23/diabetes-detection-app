import joblib
import streamlit as st
import pandas as pd


model = joblib.load('diabet_detection.pkl')

st.title('Diabets Dectection Apss', text_alignment='center')
st.markdown('Please enter your data and press predict button')

st.divider()

gender = st.selectbox('Jenis Kelamin', ['Laki-laki', 'Perempuan'])
age = st.number_input('Umur: ', min_value=0, value=0)
hypertension = st.number_input(
    'Apakah tekanan darah anda tiggi (Yes: 1, No: 0)', min_value=0, value=0, max_value=1, help="Hanya masukkan 0 atau 1")
heart_disease = st.number_input(
    'Apakah anda memiliki riwayat sakit jantung ( Yes: 1, No: 0)', min_value=0, value=0, max_value=1, help="Hanya masukkan 0 atau 1")
smoking_history = st.selectbox('Apakah anda merokok', [
                               'Iya', 'Tidak ingat', 'Tidak'])
bmi = st.number_input('Index masa tubuh', value=0.00, min_value=0.00,
                      help="BMI = berat badan (kg) / (tinggi badan (m))²")
HbA1c_level = st.number_input(
    'Rata-rata kadar gula darah 2–3 bulan terakhir', min_value=0.0, value=0.0)
blood_glucose_level = st.number_input(
    'Kadar gula darah(mg/dL)', min_value=0, value=0)


if st.button('Predict'):
    input_data = pd.DataFrame([{
        'gender': gender,
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'smoking_history': smoking_history,
        'bmi': bmi,
        'HbA1c_level': HbA1c_level,
        'blood_glucose_level': blood_glucose_level
    }])

    prediction = model.predict(input_data)[0]
    st.subheader(f'Prediction: {(prediction)}')
    if prediction == 1:
        st.error('Kemungkinan besar anda mengidap diabetes')
    else:
        st.success("Kemungkinan besar anda tidak mengidap diabetes")
