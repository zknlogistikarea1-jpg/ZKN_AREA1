import streamlit as st
import pandas as pd

# 1. Konfigurasi Dasar
st.set_page_config(page_title="LOGISTIC HELPER APP", layout="wide")

# 2. CSS untuk Card Klik-able tanpa Tombol Terlihat
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }

    .header-container { text-align: center; padding: 50px 0 30px 0; }
    .main-title {
        font-size: 45px; font-weight: 800;
        background: linear-gradient(90deg, #FF4B2B 0%, #DC3545 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-title { font-size: 18px; color: #57606f; }

    /* Container Card Utama */
    .card-container {
        position: relative;
        background: #ffffff;
        border-radius: 24px;
        padding: 40px 20px;
        text-align: center;
        border: 1px solid #f1f2f6;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        transition: all 0.4s ease;
        height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }

    .card-container:hover {
        transform: translateY(-12px);
        box-shadow: 0 20px 40px rgba(220, 53, 69, 0.2);
        border-color: #DC3545;
    }

    .icon-circle {
        width: 80px; height: 80px;
        background: #FFF5F5; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 40px; margin-bottom: 20px; transition: 0.3s;
    }

    .card-container:hover .icon-circle { background: #DC3545; color: white !important; }
    .card-title { font-weight: 800; font-size: 18px; color: #2f3542; margin-bottom: 10px; text-transform: uppercase; }
    .card-desc { font-size: 13px; color: #747d8c; line-height: 1.5; }

    /* Membuat Tombol Streamlit menjadi Transparan & Menutupi Seluruh Card */
    .stButton > button {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 300px;
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        z-index: 10;
        cursor: pointer;
    }
    
    /* Menghilangkan efek hover bawaan tombol agar tidak merusak desain card */
    .stButton > button:hover { background: transparent !important; color: transparent !important; }
    .stButton > button:active { background: transparent !important; color: transparent !important; }
    .stButton > button:focus { box-shadow: none !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <h1 class="main-title">Layanan Utama</h1>
        <p class="sub-title">Kelola Operasional Logistik Area 1 • SamLog Helper</p>
    </div>
    """, unsafe_allow_html=True)

# Grid Menu Utama
col1, col2, col3, col4 = st.columns(4)

with col1:
    # Div Visual (Desain Card)
    st.markdown("""
        <div class="card-container">
            <div class="icon-circle">🏷️</div>
            <div class="card-title">Cetak ID Koli</div>
            <p class="card-desc">Filter Stok 0% dan<br>Transformasi Data Koli</p>
        </div>
    """, unsafe_allow_html=True)
    # Tombol Transparan (Logika Klik)
    if st.button("", key="btn_koli"):
        st.switch_page("pages/Cetak_ID_Koli.py")

with col2:
    st.markdown("""
        <div class="card-container">
            <div class="icon-circle">📦</div>
            <div class="card-title">Stock In</div>
            <p class="card-desc">Compare Data, Split PO,<br>dan Cek Stock Level</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("", key="btn_stock"):
        st.info("Fitur Stock In sedang disiapkan")

with col3:
    st.markdown("""
        <div class="card-container">
            <div class="icon-circle">👞</div>
            <div class="card-title">Peminjaman</div>
            <p class="card-desc">Monitoring Peminjaman<br>Sepatu & Sandal Kerja</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("", key="btn_pinjam")

with col4:
    st.markdown("""
        <div class="card-container">
            <div class="icon-circle">📋</div>
            <div class="card-title">Surat Jalan</div>
            <p class="card-desc">Pencatatan & Monitoring<br>Surat Jalan RTO</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("", key="btn_sj")