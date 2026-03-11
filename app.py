import streamlit as st

# 1. Konfigurasi
st.set_page_config(page_title="LOGISTIC HELPER APP", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS Master (Menjamin Seluruh Area Kartu Bisa Diklik)
st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none;}
    .stApp { background-color: #FFFFFF !important; }

    .header-container { text-align: center; padding: 40px 0; }
    .main-title { font-size: 45px; font-weight: 800; color: #DC3545; }

    /* Container Kartu */
    .card-wrapper {
        position: relative;
        height: 320px; /* Tinggi kartu */
        width: 100%;
    }

    /* Desain Kartu Visual */
    .card-visual {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: #ffffff;
        border-radius: 24px;
        border: 1px solid #f1f2f6;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transition: all 0.3s ease;
        z-index: 1; /* Di bawah tombol */
    }

    /* Efek Nyala saat Mouse di atas Kartu */
    .card-wrapper:hover .card-visual {
        transform: translateY(-10px);
        border-color: #DC3545;
        box-shadow: 0 20px 40px rgba(220, 53, 69, 0.15);
    }

    .icon-circle {
        width: 80px; height: 80px;
        background: #FFF5F5; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 40px; margin-bottom: 20px;
    }

    .card-title { font-weight: 800; font-size: 18px; color: #2f3542; margin-bottom: 10px; }
    .card-desc { font-size: 14px; color: #747d8c; text-align: center; padding: 0 15px; }

    /* TOMBOL TRANSPARAN - Menutupi seluruh kartu secara mutlak */
    .stButton > button {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 320px !important; /* Harus sama dengan card-wrapper */
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        z-index: 10 !important; /* Harus paling atas agar bisa diklik */
        cursor: pointer;
    }
    
    .stButton > button:hover, .stButton > button:active, .stButton > button:focus {
        background: transparent !important;
        color: transparent !important;
        box-shadow: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <h1 class="main-title">Layanan Utama</h1>
        <p style="color:#57606f; font-size: 18px;">Kelola Operasional Logistik Area 1 • SamLog Helper</p>
    </div>
    """, unsafe_allow_html=True)

# Grid Menu
col1, col2, col3, col4 = st.columns(4)

def create_card(col, icon, title, desc, page_name, k):
    with col:
        # Kita buka pembungkus kartu
        st.markdown(f"""
            <div class="card-wrapper">
                <div class="card-visual">
                    <div class="icon-circle">{icon}</div>
                    <div class="card-title">{title}</div>
                    <div class="card-desc">{desc}</div>
                </div>
        """, unsafe_allow_html=True)
        
        # Tombol Streamlit diletakkan di SINI. 
        # Karena CSS 'absolute', dia akan otomatis 'terbang' ke atas menutupi div kartu.
        if st.button(" ", key=k):
            st.switch_page(f"pages/{page_name}.py")
            
        # Kita tutup pembungkus kartu
        st.markdown("</div>", unsafe_allow_html=True)

# Panggil fungsi untuk tiap menu
create_card(col1, "🏷️", "Cetak ID Koli", "Filter Stok 0% &<br>Transformasi Data", "Cetak_ID_Koli", "c1")
create_card(col2, "📦", "Stock In", "Compare Data, Split PO,<br>& Stock Level", "Stock_In", "c2")
create_card(col3, "👞", "Peminjaman", "Monitoring Sepatu<br>& Sandal Kerja", "Stock_In", "c3")
create_card(col4, "📋", "Surat Jalan", "Pencatatan &<br>Monitoring RTO", "Stock_In", "c4")