import streamlit as st
import pandas as pd

st.set_page_config(page_title="CETAK ID KOLI", layout="wide")

st.markdown("<h2 style='text-align: center; color: #DC3545;'>🏷️ MODUL CETAK ID KOLI</h2>", unsafe_allow_html=True)
st.write("---")

if st.button("⬅️ Kembali ke Menu Utama"):
    st.switch_page("app.py")

uploaded_file = st.file_uploader("Import File Excel (Koli)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, skiprows=1)
    df['%'] = df['%'].astype(str)
    filtered_df = df[df['%'].str.contains('0')]

    st.success(f"Berhasil memfilter {len(filtered_df)} data.")
    st.dataframe(filtered_df, use_container_width=True)