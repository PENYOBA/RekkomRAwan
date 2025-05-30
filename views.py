import streamlit as st
import controllers.methods as methods
from sympy import sympify
import numpy as np
import time

def display_home():
    
    st.write("""
            Selamat datang di Homepage metode mencari akar. Pilih metode yang ingin digunakan pada menu di sebelah kiri.
            Dashboard ini dibuat oleh Kelompok 6 untuk memenuhi tugas mata kuliah Rekayasa Komputasional
            
            Anggota Kelompok :
            1. Annisa Amirah Abdillah (50422233)
            2. Katharina Stasiama Sarto (50422769)
            3. Muhammad Afwan Sudiro (50422973)
            4. Muhammad Aidil Kusumayadi (50422974)
            5. Raihan Musyaffa Hanif (51422357)
            """)
    
    st.markdown(
        """
        #### Metode yang Tersedia:
        """
    )
    
    st.image("assets/metode-pencarian-akar.jpg", use_container_width=False, width=500)

def display_bisection():
    st.subheader("Metode Bisection (Bagi Dua)")
    st.write("Metode ini mencari akar fungsi dengan membagi interval [a, b] menjadi dua bagian secara bertahap, kemudian memilih bagian yang mengandung akar.")
    
    st.markdown(
        """
        ###### Rumus:
        $$c = \\frac{a + b}{2}$$
        
        Dimana:
        - $a$ dan $b$ adalah batas interval, 
        - $c$ adalah titik tengah yang diperiksa. 
        - Jika $f(a) \cdot f(c) < 0$, maka akar berada di interval $[a, c]$,
        - Jika $f(a) \cdot f(c) > 0$, maka akar berada di interval $[c, b]$.
        """
    )
    
    
    # Input for function
    func = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input for interval
    a = st.text_input("Masukkan nilai a:", value="0.0")
    a = np.float64(a)
    b = st.text_input("Masukkan nilai b:", value="5.0")
    b = np.float64(b)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
     
    if st.button("Hitung"):
        with st.spinner("Sedang Menghitung...", show_time=True):
            time.sleep(1)
            st.success("Selesai!")
        result = methods.biseksi(a, b, func, e)
        hasil.write(f"Hasil Akar : {result}")
        
def display_regula_falsi():
    st.subheader("Metode Regula Falsi")
    st.write("Metode ini menggunakan garis lurus yang menghubungkan dua titik pada grafik fungsi dan memperkirakan akar pada titik potong garis tersebut dengan sumbu x.    ")
    
    st.markdown(
        """
        ###### Rumus:
        $$x = \\frac{b \\cdot f(a) - a \\cdot f(b)}{f(a) - f(b)}$$
        
        Dimana $a$ dan $b$ adalah dua titik, dan $f(a)$ serta $f(b)$ adalah nilai fungsi pada titik tersebut.
        """
    )
    
    # Input for function
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input for interval
    a = st.text_input("Masukkan nilai a:", value="0.0")
    a = np.float64(a)
    b = st.text_input("Masukkan nilai b:", value="5.0")
    b = np.float64(b)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
    
    if st.button("Hitung"):
        with st.spinner("Sedang Menghitung...", show_time=True):
            time.sleep(1)
            st.success("Selesai!")
        result = methods.regula_falsi(a, b, f_x, e)
        hasil.write(f"Hasil Akar : {result}")
        
def display_iterasi_sederhana():
    st.subheader("Metode Iterasi Sederhana")
    st.write("Metode ini menggunakan persamaan iteratif untuk mendekati akar, dengan memasukkan nilai yang dihitung pada iterasi sebelumnya.")
    
    st.markdown(
        """
            ###### Permasalahan: $x^2 - 2x - 3 = 0$
        """
    )
    
    st.write("Ada 3 kemungkinan yang dapat digunakan untuk menyelesaikan permasalahan di atas, yaitu:")
    
    st.markdown(
        """
            - $x = \\sqrt{2x + 3}$
            - $x = \\frac{3}{x - 2}$
            - $x = \\frac{x^2 - 3}{2}$
        """
    )
    
    x_initial = st.text_input("Masukkan nilai x awal:", value="0.0")
    x_initial = np.float64(x_initial)
    max_iter = st.number_input("Masukkan jumlah iterasi maksimum:", value=100)
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    cols = st.empty()
    
    if st.button("Hitung"):
        with st.spinner("Sedang Menghitung...", show_time=True):
            time.sleep(1)
            st.success("Selesai!")
        col1, col2, col3 = cols.columns(3)
        
        with col1:
            result1 = methods.iterasi_sederhana(x_initial, "sqrt(2*x + 3)", e, max_iter)
            col1.metric(f"Hasil Akar (x = sqrt(2x + 3))", result1, border=True)
        with col2:
            result2 = methods.iterasi_sederhana(x_initial, "3 / (x - 2)", e, max_iter)
            col2.metric(f"Hasil Akar (x = 3 / (x - 2))", result2, border=True)
        with col3:
            result3 = methods.iterasi_sederhana(x_initial, "(x**2 - 3) / 2", e, max_iter)
            col3.metric(f"Hasil Akar (x = (x^2 - 3) / 2)", result3, border=True)



def display_newton_raphson():
    st.subheader("Metode Newton Raphson")
    st.write("Metode Newton Raphson adalah metode numerik untuk mencari akar dari fungsi dengan cara menggunakan turunan fungsi.")
    
    st.markdown(
        """
        ###### Rumus:
        $$x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}$$
        
        Dimana $f(x_n)$ adalah nilai fungsi pada $x_n$, dan $f'(x_n)$ adalah turunan pertama dari fungsi tersebut.
        """
    )
    
    # Input for function
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x - exp(-x)")
    f_x = sympify(f_x)
    
    # Input for initial guess
    x0 = st.text_input("Masukkan nilai x awal:", value="0.0")
    x0 = np.float64(x0)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.00001")
    e = np.float64(e)
    
    hasil = st.empty()
    
    if st.button("Hitung"):
        with st.spinner("Sedang Menghitung...", show_time=True):
            time.sleep(1)
            st.success("Selesai!")
        result = methods.newton_raphson(x0, f_x, e)
        hasil.write(f"Hasil Akar : {result}")

def display_secant():
    st.subheader("Metode Secant")
    st.write("Metode Secant adalah metode numerik untuk mencari akar dari fungsi dengan cara menggunakan dua titik pada grafik fungsi.")
    
    st.markdown(
        """
        ###### Rumus:
        $$x_{n+1} = x_n - \\frac{f(x_n) \\cdot (x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}$$
        
        Dimana $x_n$ dan $x_{n-1}$ adalah dua titik yang digunakan dalam perhitungan akar.
        """
    )
        
    # Input for function
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input for initial guesses
    x0 = st.text_input("Masukkan nilai x0:", value="0.0")
    x0 = np.float64(x0)
    x1 = st.text_input("Masukkan nilai x1:", value="5.0")
    x1 = np.float64(x1)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
    
    if st.button("Hitung"):
        with st.spinner("Sedang Menghitung...", show_time=True):
            time.sleep(1)
            st.success("Selesai!")
        result = methods.secant(x0, x1, f_x, e)
        hasil.write(f"Hasil Akar : {result}")

