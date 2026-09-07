import streamlit as st
import os

st.set_page_config(page_title="Premium Notes Portal", page_icon="📚", layout="centered")

st.title("🚀 Premium Notes Portal")
st.write("---")

st.info("🎯 **Aapke Notes Aur PYQs Yahan Hain!**")
st.write("Dropdown menu se apna chapter select karein aur neeche diye gaye button se download karein.")
st.write("")

# 1. Bina kisi API ya internet link ke direct folder scan karna
all_files = os.listdir(".")
# 2. Sirf aur sirf .pdf files ko apne aap alag karna
pdf_files = [f for f in all_files if f.endswith(".pdf")]

if pdf_files:
    pdf_files.sort()
    
    # Dropdown menu me clean naam dikhane ke liye
    display_names = [f.replace(".pdf", "").replace("_", " ") for f in pdf_files]
    
    # Automatic Dropdown Menu
    selected_display = st.selectbox("📑 Select Chapter / Note", display_names)
    
    # Asli file ka naam select karna
    actual_file_name = pdf_files[display_names.index(selected_display)]
    
    # File ko binary me read karna (Bina kisi network error ke sabse safe tarika)
    with open(actual_file_name, "rb") as file:
        pdf_bytes = file.read()
    
    st.write("")
    
    # Streamlit ka official fully optimized premium download button
    st.download_button(
        label=f"📥 Download: {selected_display}",
        data=pdf_bytes,
        file_name=actual_file_name,
        mime="application/pdf",
        use_container_width=True
    )
else:
    st.warning("⚠️ GitHub repository me abhi koi bhi .pdf file nahi mili hai.")

st.write("---")
st.caption("Developed for Class 9th & 10th Students.")
