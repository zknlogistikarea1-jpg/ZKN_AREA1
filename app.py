import streamlit as st

# 1. Setting Dasar
st.set_page_config(page_title="LOGISTIC HELPER", layout="wide", initial_sidebar_state="collapsed")

# 2. SATU-SATUNYA PERINTAH UNTUK TAMPILAN
st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none;}
    .stApp { background-color: #FFFFFF !important; }
    .header-container { text-align: center; padding: 40px 0; font-family: sans-serif; }
    .main-title { font-size: 45px; font-weight: 800; color: #DC3545; margin: 0; }
    .main-menu-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        padding: 20px;
        max-width: 1200px;
        margin: 0 auto;
        font-family: sans-serif;
    }
    .menu-card {
        text-decoration: none !important;
        background: #ffffff;
        border-radius: 24px;
        border: 1px solid #f1f2f6;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 25px;
        transition: all 0.3s ease;
        color: #2f3542 !important;
    }
    .menu-card:hover {
        transform: translateY(-10px);
        border-color: #DC3545;
        box-shadow: 0 20px 40px rgba(220, 53, 69, 0.15);
    }
    .icon-box { font-size: 60px; margin-bottom: 20px; }
    .title-box { font-weight: 800; font-size: 22px; margin-bottom: 12px; }
    .desc-box { font-size: 14px; color: #747d8c; line-height: 1.5; }
    </style>

    <div class="header-container">
        <h1 class="main-title">Layanan Utama</h1>
        <p style="color:#57606f; font-size:18px;">Operasional Logistik Area 1</p>
    </div>

    <div class="main-menu-grid">
        <a href="/Cetak_ID_Koli" target="_self" class="menu-card">
            <div class="icon-box">🏷️</div>
            <div class="title-box">Cetak ID Koli</div>
            <div class="desc-box">Filter Stok 0% & Transformasi Data</div>
        </a>
        <a href="/Stock_In" target="_self" class="menu-card">
            <div class="icon-box">📦</div>
            <div class="title-box">Stock In</div>
            <div class="desc-box">Compare Data & Split PO</div>
        </a>
        <a href="/Peminjaman" target="_self" class="menu-card">
            <div class="icon-box">👞</div>
            <div class="title-box">Peminjaman</div>
            <div class="desc-box">Monitoring Sepatu & Sandal</div>
        </a>
        <a href="/Surat_Jalan" target="_self" class="menu-card">
            <div class="icon-box">📋</div>
            <div class="title-box">Surat Jalan</div>
            <div class="desc-box">Pencatatan & Monitoring RTO</div>
        </a>
    </div>
""", unsafe_allow_html=True)