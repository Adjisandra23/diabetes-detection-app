import streamlit as st

st.set_page_config(
    page_title="Diabetes Detection Website",
    layout='wide'
)

st.title("Welcome to Diabetes Detection App", text_alignment='center')
st.write("Gunakan menu di sebelah kiri-atas untuk navigasi")

st.divider()
col1, col2 = st.columns(2)

with col1:
    st.image("assets/image1.png")

with col2:
    st.image("assets/image2.png")


st.divider()
col3, col4 = st.columns(2)

with col3:
    st.image("assets/image3.png")

with col4:
    st.image("assets/image4.png")


st.divider()
col5, col6 = st.columns(2)

with col5:
    st.image("assets/image5.png")

with col6:
    st.image("assets/image6.png")


st.divider()
col7, col8 = st.columns(2)

with col7:
    st.image("assets/image7.png")

with col8:
    st.image("assets/image8.png")


st.divider()
col9, col10 = st.columns(2)

with col9:
    st.image("assets/image9.png")

with col10:
    st.image("assets/image10.png")
