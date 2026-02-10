import streamlit as st

st.title("Home", text_alignment='center')
st.write("Website ini dibuat untuk memprediksi risiko diabetes berdasarkan beberapa indikator kesehatan. Dengan mengisi data yang diminta, pengguna dapat memperoleh prediksi mengenai kemungkinan mereka mengidap diabetes. Harap diingat bahwa hasil prediksi ini bersifat indikatif dan tidak menggantikan diagnosis medis profesional. Untuk informasi lebih lanjut, silakan kunjungi halaman 'Prediction' di menu sebelah kiri.")

st.divider()
st.subheader("Pengantar")
st.write(" Diabetes merupakan salah satu penyakit tidak menular yang jumlah penderitanya terus meningkat dari tahun ke tahun. Di Indonesia, diabetes telah menjadi masalah kesehatan serius karena sering kali tidak disadari sejak dini dan baru terdeteksi ketika sudah menimbulkan komplikasi. Perubahan gaya hidup, pola makan yang tidak sehat, kurangnya aktivitas fisik, serta faktor usia dan genetik menjadi penyebab utama meningkatnya kasus diabetes di masyarakat. Seiring dengan perkembangan teknologi, deteksi dini menjadi langkah penting untuk mencegah dampak yang lebih serius. Oleh karena itu, website ini dibuat sebagai alat bantu untuk memprediksi risiko diabetes sejak dini berdasarkan beberapa indikator kesehatan. Dengan adanya website ini, diharapkan pengguna dapat lebih sadar terhadap kondisi kesehatannya dan mengambil langkah pencegahan lebih awal sebelum diabetes berkembang lebih lanjut.")

st.divider()
st.subheader("Panduan Pengisian Data Prediksi Diabetes")
st.write("Untuk membantu Anda memahami hasil prediksi dengan lebih akurat, silakan isi data berikut sesuai dengan kondisi Anda saat ini. Berikut penjelasan dari setiap data yang perlu diisi:")

st.divider()

st.subheader("1. Gender (Jenis Kelamin)")
st.write("Pilih jenis kelamin Anda")
st.write("Male → Laki-laki")
st.write("Female → Perempuan")
st.write("Jenis kelamin dapat memengaruhi risiko diabetes karena perbedaan hormon dan metabolisme tubuh")

st.subheader("2. Age (Umur)")
st.write("Masukkan umur Anda dalam tahun")
st.write("Risiko diabetes cenderung meningkat seiring bertambahnya usia, terutama setelah usia 45 tahun")

st.subheader("3. Hypertension (Tekanan Darah Tinggi)")
st.write("Masukkan 1 jika Anda memiliki tekanan darah tinggi, atau 0 jika tidak")
st.write("Tekanan darah tinggi dapat meningkatkan risiko komplikasi diabetes dan memengaruhi kesehatan jantung")

st.subheader("4. Heart Disease (Riwayat Penyakit Jantung)")
st.write("Masukkan 1 jika Anda memiliki riwayat penyakit jantung, atau 0 jika tidak")
st.write("Penyakit jantung sering kali terkait dengan diabetes, sehingga riwayat penyakit jantung dapat menjadi indikator penting")

st.subheader("5. Smoking History (Riwayat Merokok)")
st.write("Pilih salah satu dari opsi berikut:")
st.write("Yes → Iya")
st.write("No → Tidak")
st.write("Smoking dapat merusak pembuluh darah dan meningkatkan risiko resistensi insulin, yang berkontribusi pada perkembangan diabetes")

st.subheader("6. BMI (Indeks Massa Tubuh)")
st.write("Masukkan nilai BMI Anda. BMI dihitung dengan rumus: berat badan (kg) / (tinggi badan (m))²")
st.write("BMI adalah indikator penting untuk menilai kelebihan berat badan atau obesitas, yang merupakan faktor risiko utama untuk diabetes tipe 2")
st.markdown("Contoh: ")

weight = st.number_input("Berat Badan (kg)", min_value=0.0)
height = st.number_input("Tinggi Badan (cm)", min_value=0.0)

if st.button("Hitung BMI"):
    if height > 0:
        bmi = weight / (height / 100) ** 2
        st.success(f"BMI Anda: {bmi:.2f}")
    else:
        st.warning("Tinggi badan harus lebih dari 0")

st.markdown("Kategori BMI:")
st.markdown("< 18.5 → Berat badan kurang")
st.markdown("18.5 - 24.9 → Normal")
st.markdown("25 - 29.9 → Kelebihan berat badan")
st.markdown("≥ 30 → Obesitas")
st.markdown("Semakin tinggi BMI, semakin besar risiko diabetes.")


st.subheader("7. HbA1c Level (Rata-rata Kadar Gula Darah 2-3 Bulan Terakhir)")
st.write("Masukkan nilai HbA1c Anda dalam persen (%)")
st.write("HbA1c mencerminkan rata-rata kadar gula darah Anda selama 2-3 bulan terakhir. Nilai HbA1c yang tinggi menunjukkan kontrol gula darah yang buruk dan risiko diabetes yang lebih tinggi")
st.markdown("Nilai umum:")
st.markdown("< 5.7 → Normal")
st.markdown("5.7 - 6.4 → Prediabetes")
st.markdown("≥ 6.5 → Diabetes")

st.subheader("8. Blood Glucose Level (Kadar Gula Darah)")
st.write("Masukkan kadar gula darah Anda dalam mg/dL")
st.write("Kadar gula darah yang tinggi dapat menjadi indikator langsung dari diabetes. Pengukuran ini penting untuk menilai risiko diabetes dan efektivitas pengelolaan gula darah")
