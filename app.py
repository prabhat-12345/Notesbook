import streamlit as st
import os
from streamlit_pdf_viewer import pdf_viewer

# Premium wide layout setup
st.set_page_config(page_title="Premium Notes Viewer", page_icon="📚", layout="wide")

st.title("🚀 Premium Notes Portal")
st.write("---")

st.info("🎯 **Bina download kiye aap yahan direct notes scroll karke padh sakte hain!**")

# 1. Local folder se saari .pdf files automatic scan karna
all_files = os.listdir(".")
pdf_files = [f for f in all_files if f.endswith(".pdf")]

if pdf_files:
    pdf_files.sort()
    
    # Dropdown menu ke liye clean naam
    display_names = [f.replace(".pdf", "").replace("_", " ") for f in pdf_files]
    
    selected_display = st.selectbox("📑 Padhne ke liye Chapter chunein:", display_names)
    actual_file_name = pdf_files[display_names.index(selected_display)]
    
    st.write(f"### 📖 Now Reading: {selected_display}")
    st.write("---")
    
    # 2. Bina kisi external URL ya network connection ke PDF dikhane ka naya component
    # Yeh mobile browser par 100% chalega bina block hue
    with open(actual_file_name, "rb") as f:
        pdf_data = f.read()
        
    pdf_viewer(input=pdf_data, height=700, width=800)
    
    st.write("---")
    
    # Backup download option niche
    st.download_button(
        label=f"📥 Mere phone me download karein",
        data=pdf_data,
        file_name=actual_file_name,
        mime="application/pdf",
        use_container_width=True
    )
else:
    st.warning("⚠️ GitHub repository me abhi koi bhi .pdf file nahi mili hai.")

st.write("---")
st.caption("Developed for Class 9th & 10th Students.")
