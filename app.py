import streamlit as st
import time

# Konfigurasi Halaman
st.set_page_config(page_title="Cinemorph AI Web", layout="wide")

# --- SIDEBAR: PENGATURAN FILM ---
st.sidebar.header("🎬 Konfigurasi Film")
num_scenes = st.sidebar.slider("Jumlah Adegan (Scenes)", 1, 10, 3)
style = st.sidebar.selectbox("Pilih Gaya Visual", [
    "Pixar Style", "Unreal Engine 5", "Anime Style", 
    "Studio Ghibli", "Stop Motion", "Chibi Toys", "3D Animation"
])

# --- MAIN INTERFACE ---
st.title("🚀 Cinemorph AI Movie Maker")
st.subheader("Ubah Ide Cerita Menjadi Film Animasi")

# Input Naskah
story_prompt = st.text_area("Tulis naskah atau premis cerita Anda:", 
                            placeholder="Contoh: Seekor kucing astronot menemukan planet yang terbuat dari keju...")

col1, col2 = st.columns(2)

with col1:
    if st.button("✨ 1. Generate Storyboard (Gambar)"):
        st.write(f"### Memproses {num_scenes} Adegan...")
        # Simulasi proses AI pembuat gambar
        progress_bar = st.progress(0)
        for i in range(num_scenes):
            time.sleep(0.5) # Simulasi loading
            st.image(f"https://picsum.photos/seed/{i+10}/800/450", caption=f"Adegan {i+1} - Gaya: {style}")
            progress_bar.progress((i + 1) / num_scenes)
        st.success("Storyboard Berhasil Dibuat!")

with col2:
    if st.button("🎥 2. Render Menjadi Video"):
        with st.spinner("Sedang memproses video... Harap tunggu."):
            time.sleep(3) # Simulasi proses AI Video
            
            # Tampilan Video (Simulasi)
            st.video("https://www.w3schools.com/html/mov_bbb.mp4") # Video contoh
            
            st.divider()
            
            # --- FITUR DOWNLOAD (Sesuai Permintaan) ---
            st.write("### ✅ Film Selesai! Silakan Download:")
            
            # Tombol Download Video
            st.download_button(
                label="📥 Download Hasil Video (.MP4)",
                data="Ini adalah data video dummy", # Ganti dengan data biner video asli nantinya
                file_name="film_karya_saya.mp4",
                mime="video/mp4"
            )
            
            # Tombol Download Semua Gambar
            st.download_button(
                label="🖼️ Download Semua Gambar Adegan (ZIP)",
                data="Data gambar dummy",
                file_name="storyboard_images.zip",
                mime="application/zip"
            )

# --- FOOTER ---
st.info("Aplikasi ini menggunakan teknologi AI untuk mengubah teks menjadi visual.")
