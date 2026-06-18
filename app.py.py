
import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

# 1. Konfigurasi Halaman & Judul
st.set_page_config(page_title="DataGuess Game", page_icon="📈")
st.title("📈 DataGuess: Game Tebak Angka & Statistik")

# Teks Penjelasan/Pengantar Game
st.markdown("""
Selamat datang di **DataGuess**! Ini adalah proyek kolaborasi kami yang menggabungkan konsep game sederhana dengan analisis data visual.
* **Misi Anda:** Tebak angka rahasia antara **1 sampai 100** yang dipilih acak oleh komputer.
* **Fitur Keren:** Setiap tebakan Anda akan langsung dicatat, dianalisis, dan digambarkan dalam grafik interaktif di bawah!
---
""")

# 2. Inisialisasi Memori Game
if "angka_rahasia" not in st.session_state:
    st.session_state.angka_rahasia = random.randint(1, 100)
    st.session_state.riwayat_tebakan = []

# 3. Input dari Pemain & Instruksi Teks
st.subheader("🎮 Mulai Bermain")
tebakan = st.number_input("Masukkan angka tebakanmu di sini, lalu klik 'Cek Angka':", min_value=1, max_value=100, step=1)

# 4. Tombol Cek Angka & Teks Feedback
if st.button("Cek Angka"):
    st.session_state.riwayat_tebakan.append(tebakan)

    if tebakan < st.session_state.angka_rahasia:
        st.warning(f"📉 **Tebakan ({tebakan}) Terlalu RENDAH!** Coba masukkan angka yang lebih besar.")
    elif tebakan > st.session_state.angka_rahasia:
        st.warning(f"📈 **Tebakan ({tebakan}) Terlalu TINGGI!** Coba masukkan angka yang lebih kecil.")
    else:
        st.success(f"🎉 **SANGAT AKURAT!** Angka rahasianya memang **{st.session_state.angka_rahasia}**!")
        st.balloons()

        # Teks Evaluasi Performa berdasarkan jumlah percobaan
        skor = len(st.session_state.riwayat_tebakan)
        st.markdown(f"### 🏆 Evaluasi Performa Anda:")
        if skor <= 5:
            st.write(f"Sempurna! Anda berhasil menebak dalam **{skor} kali percobaan**. Anda adalah seorang *Data Wizard*! 🧙‍♂️")
        elif skor <= 10:
            st.write(f"Bagus sekali! Anda berhasil menebak dalam **{skor} kali percobaan**. Strategi yang cukup baik! 👍")
        else:
            st.write(f"Berhasil! Anda menebak dalam **{skor} kali percobaan**. Lain kali, gunakan strategi eliminasi nilai tengah ya! 🧐")

# 5. Tampilkan Grafik & Data (Jika sudah ada tebakan)
if st.session_state.riwayat_tebakan:
    st.markdown("---")
    st.subheader("📊 Papan Analisis Data & Grafik")
    st.write("Teks analitik: Grafik di bawah menunjukkan tren tebakan Anda (garis biru) dibandingkan dengan target angka rahasia (garis putus-putus merah).")

    # Menggunakan Pandas untuk mengolah riwayat
    df = pd.DataFrame({
        "Percobaan Ke-": range(1, len(st.session_state.riwayat_tebakan) + 1),
        "Angka Tebakan": st.session_state.riwayat_tebakan
    })

    # Membuat Grafik dengan Matplotlib
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(df["Percobaan Ke-"], df["Angka Tebakan"], marker='o', color='b', label='Tebakanmu')
    ax.axhline(y=st.session_state.angka_rahasia, color='r', linestyle='--', label='Angka Rahasia')
    ax.set_xlabel("Percobaan Ke-")
    ax.set_ylabel("Nilai Angka")
    ax.legend()
    ax.grid(True)

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)

    # Menampilkan tabel data berupa teks ringkasan di bawahnya
    st.write("**Tabel Riwayat Data Tebakan:**")
    st.dataframe(df.set_index("Percobaan Ke-"))

# 6. Tombol Reset dengan Informasi Teks
st.markdown("---")
st.write("Ingin mengulang permainan atau mengganti angka rahasia baru?")
if st.button("🔄 Main Lagi / Reset Game"):
    st.session_state.angka_rahasia = random.randint(1, 100)
    st.session_state.riwayat_tebakan = []
    st.rerun()

# 7. Footer Kolaborasi (Teks Kredit Tim)
st.markdown("---")
st.caption("Proyek ini dikembangkan menggunakan **Streamlit**, **Matplotlib**, dan **Pandas**[cite: 1].")
st.caption("Dibuat dengan 💻 oleh Tim Kolaborasi: **[Nama Anda]** & **[Nama Tempa Anda]**")
