import streamlit as st
import pandas as pd

# 1. KONFIGURASI HALAMAN (Wajib paling atas)
st.set_page_config(
    page_title="STOCK IN PROCESSING", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. CSS SAKTI (Memaksa Putih, Judul Merah, & Tombol Pojok)
st.markdown("""
    <style>
    /* 1. Paksa Background Putih Bersih */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: white !important;
    }

    /* 2. Judul Utama Merah */
    .main-title {
        color: #DC3545;
        font-weight: 800;
        font-size: 32px;
        margin-top: -60px; /* Menarik judul ke atas agar pas */
    }

    /* 3. Paksa Semua Teks Jadi Hitam */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: black !important;
    }

    /* 4. Tombol Kembali (Home) di Pojok Kanan Atas */
    div.stButton > button[key="home_fix"] {
        position: fixed;
        top: 15px;
        right: 60px; /* Menghindari tertutup menu Streamlit */
        width: 45px !important;
        height: 45px !important;
        background-color: #DC3545 !important;
        color: white !important;
        border-radius: 50% !important;
        border: none !important;
        font-size: 20px !important;
        z-index: 999999;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    div.stButton > button[key="home_fix"]:hover {
        background-color: #a71d2a !important;
    }

    /* 5. Tombol Proses Utama (Merah Lebar) */
    div.stButton > button[key="btn_proses"] {
        background-color: #DC3545 !important;
        color: white !important;
        width: 100% !important;
        border-radius: 8px !important;
        height: 50px;
        font-weight: bold;
        border: none !important;
    }

    /* 6. Kotak Upload File */
    [data-testid="stFileUploadDropzone"] {
        border: 2px dashed #DC3545 !important;
        background-color: #fff5f5 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- AREA NAVIGASI ---
# Tombol ini akan otomatis pindah ke pojok kanan atas karena CSS di atas
if st.button("⬅️", key="home_fix"):
    st.switch_page("app.py")

# --- JUDUL ---
st.markdown("<p class='main-title'>📦 STOCK IN PROCESSING</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #f0f2f6;'>", unsafe_allow_html=True)

# --- KONTEN UTAMA ---
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### **📥 Input Data**")
    
    files_po = st.file_uploader("DATA PO (Bisa pilih banyak)", accept_multiple_files=True, type=['xlsx'])
    file_scan = st.file_uploader("DATA SCAN", type=['xlsx'])
    file_artikel = st.file_uploader("MASTER ARTIKEL", type=['xlsx'])
    
    st.write("") # Jarak
    btn_compare = st.button("🚀 1. PROSES COMPARE", key="btn_proses")

with col2:
    st.markdown("### **📊 Pratinjau Data**")
    
    if btn_compare:
        if not files_po or not file_scan:
            st.error("⚠️ File PO dan File Scan wajib diunggah!")
        else:
            with st.spinner("Sedang memproses data..."):
                try:
                    # --- LOGIKA PANDAS ---
                    # 1. Baca Data Scan
                    df_scan = pd.read_excel(file_scan)
                    scan_map = df_scan.groupby(df_scan.columns[1])[df_scan.columns[2]].sum().to_dict()
                    
                    # 2. Baca Data PO
                    summary_compare = []
                    for f in files_po:
                        df_po = pd.read_excel(f, skiprows=1)
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
                    
                    df_final = pd.DataFrame(summary_compare)
                    
                    # Tampilkan Tabel Hasil
                    st.success("Selesai memproses!")
                    st.dataframe(
                        df_final.style.apply(
                            lambda x: ['background-color: #ffcccc' if val != 0 else '' for val in x], 
                            subset=['SELISIH'], axis=1
                        ), 
                        use_container_width=True
                    )
                except Exception as e:
                    st.error(f"Error: Format kolom Excel tidak sesuai! ({e})")