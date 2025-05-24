import streamlit as st
import views.views as views

# Cek apakah halaman pertama kali dibuka menggunakan session_state
if 'first_load' not in st.session_state:
    st.session_state.first_load = True  # Set status pertama kali dibuka

st.set_page_config(
    page_title="Metode Pencarian Akar",
    page_icon="assets/page-icon.ico",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar untuk memilih metode
with st.sidebar:
    st.title("Menu")
    
    # Tombol Homepage tetap ada di sidebar
    homepage_clicked = st.button("Homepage", icon="🏠")
    
    # Pilih Metode hanya jika Homepage tidak diklik
    SELECTION = st.selectbox(
        "Pilih Metode",
        ("Bisection", "Regula Falsi", "Iterasi Sederhana", "Newton Raphson", "Secant")
    )

# Menampilkan Homepage jika pertama kali dibuka atau jika tombol Homepage ditekan
if st.session_state.first_load or homepage_clicked:
    st.session_state.first_load = False  # Set first_load ke False setelah pertama kali
    st.title("Homepage")
    views.display_home()  # Tampilkan konten Homepage

# Menampilkan pilihan metode setelah Homepage
else:
    with st.container():
        if SELECTION == "Bisection":
            views.display_bisection()
        elif SELECTION == "Regula Falsi":
            views.display_regula_falsi()
        elif SELECTION == "Iterasi Sederhana":
            views.display_iterasi_sederhana()
        elif SELECTION == "Newton Raphson":
            views.display_newton_raphson()
        elif SELECTION == "Secant":
            views.display_secant()
