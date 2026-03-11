import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="STOCK IN PROCESSING", layout="wide")

# Gaya CSS agar mirip dengan aplikasi asli
st.markdown("""
    <style>
    .main-title { color: #DC3545; font-weight: 700; }
    .stButton>button { background-color: #DC3545; color: white; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='main-title'>📦 STOCK IN PROCESSING</h2>", unsafe_allow_html=True)

# Layout Kolom
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Input Data")
    
    # Upload File PO (Bisa banyak file)
    files_po = st.file_uploader("DATA PO (Bisa pilih banyak)", accept_multiple_files=True, type=['xlsx'])
    
    # Upload File Scan
    file_scan = st.file_uploader("DATA SCAN", type=['xlsx'])
    
    # Upload Master Artikel
    file_artikel = st.file_uploader("MASTER ARTIKEL", type=['xlsx'])
    
    btn_compare = st.button("1. PROSES COMPARE")

with col2:
    st.subheader("Pratinjau Data")
    
    if btn_compare:
        if not files_po or not file_scan:
            st.error("File PO dan File Scan wajib diunggah!")
        else:
            with st.spinner("Sedang memproses..."):
                # 1. Baca Data Scan
                df_scan = pd.read_excel(file_scan)
                # Ambil SKU (kolom 1) dan QTY (kolom 2) sesuai logika JS kamu
                scan_map = df_scan.groupby(df_scan.columns[1])[df_scan.columns[2]].sum().to_dict()
                
                # 2. Baca Data PO
                all_po_data = []
                summary_compare = []
                
                for f in files_po:
                    df_po = pd.read_excel(f, skiprows=1) # skip header sesuai JS
                    # Ambil SKU (kolom 5) dan QTY (kolom 6)
                    sku_col = df_po.columns[5]
                    qty_col = df_po.columns[6]
                    
                    po_sum = df_po.groupby(sku_col)[qty_col].sum()
                    
                    for sku, qty_po in po_sum.items():
                        qty_fisik = scan_map.get(sku, 0)
                        summary_compare.append({
                            "SKU": sku,
                            "QTY PO": qty_po,
                            "FISIK": qty_fisik,
                            "SELISIH": qty_fisik - qty_po
                        })
                
                df_final_compare = pd.DataFrame(summary_compare)
                st.write("### Hasil Compare")
                st.dataframe(df_final_compare.style.apply(lambda x: ['background-color: #ffcccc' if val != 0 else '' for val in x], subset=['SELISIH'], axis=1), use_container_width=True)
                
                # Simpan di session state agar bisa di-export
                st.session_state['data_compare'] = df_final_compare

    # Tambahkan tombol kembalike menu
    if st.button("⬅️ Kembali ke Home"):
        st.switch_page("app.py")