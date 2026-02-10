import streamlit as st

st.title("Dashboard", text_alignment='center')
st.write("Visualisasi dibawah ini merupakan hasil Explorer Data Analyst dari Model Machine Learning yang saya buat")

st.divider()

col0, col1 = st.columns(2)
with col0:
    st.image("assets/chart0.png", caption="Model Machine Learning yang Digunakan")
with col1:
    st.image("assets/chart1.png", caption="Distribusi Umur")


st.divider()

col2, col3 = st.columns(2)
with col2:
    st.image("assets/chart2.png", caption="Distribusi Tekanan Darah")
with col3:
    st.image("assets/chart3.png", caption="Distribusi BMI")


st.divider()

col4, col5 = st.columns(2)
with col4:
    st.image("assets/chart4.png", caption="Distribusi Gender")
with col5:
    st.image("assets/chart5.png", caption="Distribusi HbA1c")


st.divider()

col6, col7 = st.columns(2)
with col6:
    st.image("assets/chart6.png", caption="Distribusi Penyakit Jantung")
with col7:
    st.image("assets/chart7.png", caption="Distribusi Hypertension")


st.divider()

col8, col9 = st.columns(2)
with col8:
    st.image("assets/chart8.png", caption="Distribusi Merokok")
with col9:
    st.image("assets/chart9.png", caption="Heatmap Correlation")


st.divider()

col10, col11 = st.columns(2)
with col10:
    st.image("assets/chart10.png", caption="Accuracy Model")
with col11:
    st.image("assets/chart11.png", caption="Confusion Maxtix")
