import streamlit as st
import replicate
import os

# Ambil API Token dari Secrets
REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]

st.title("🎬 Cinemorph AI Movie Maker")

# Input Naskah & Style
story = st.text_area("Ide Cerita:", "Kucing astronot di bulan")
style = st.selectbox("Gaya Visual:", ["Pixar Style", "Studio Ghibli", "Unreal Engine 5"])
num_scenes = st.slider("Jumlah Adegan:", 1, 5, 3)

if st.button("✨ Buat Storyboard"):
    st.info("AI sedang menggambar... Harap tunggu sebentar.")
    
    # Gabungkan naskah dengan Master Prompt gaya yang kita buat tadi
    full_prompt = f"{story}, {style}, cinematic lighting, high resolution, 8k"
    
    # Panggil AI Replicate (Model SDXL)
    output = replicate.run(
        "stability-ai/sdxl:7762fd07cf271105448bc29ff551571f9f3816c1756540069956f4d0107e0594",
        input={"prompt": full_prompt, "num_outputs": num_scenes}
    )
    
    # Tampilkan Gambar Hasil AI
    for i, image_url in enumerate(output):
        st.image(image_url, caption=f"Adegan {i+1}")
        
    st.success("Gambar Original Berhasil Dibuat!")
    st.download_button("📥 Download Gambar", data=str(output), file_name="storyboard.txt")
