import streamlit as st
import os
import base64

# Premium wide layout setup
st.set_page_config(page_title="Premium Notes Viewer", page_icon="📚", layout="wide")

st.title("🚀 Premium Notes Portal")
st.write("---")

st.info("🎯 **Bina download kiye aap yahan direct notes padh sakte hain!**")

# 1. Folder se saari .pdf files automatic scan karna
all_files = os.listdir(".")
pdf_files = [f for f in all_files if f.endswith(".pdf")]

if pdf_files:
    pdf_files.sort()
    
    # Dropdown menu ke liye clean naam
    display_names = [f.replace(".pdf", "").replace("_", " ") for f in pdf_files]
    
    # Top par selection bar
    selected_display = st.selectbox("📑 Padhne ke liye Chapter chunein:", display_names)
    
    actual_file_name = pdf_files[display_names.index(selected_display)]
    
    st.write(f"### 📖 Now Reading: {selected_display}")
    
    # 2. PDF ko bina kisi external URL ke direct read karke app me embed karne ka sabse safe tarika
    with open(actual_file_name, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # Streamlit ka apna internal PDF displayer component (Bina kisi network error ke 100% chalega)
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" style="border: 2px solid #0072ff; border-radius: 10px;"></iframe>'
    
    st.markdown(pdf_display, unsafe_allow_html=True)
    
    st.write("---")
    
    # Backup download option niche
    with open(actual_file_name, "rb") as file:
        pdf_bytes = file.read()
    st.download_button(
        label=f"📥 Mere phone me download karein",
        data=pdf_bytes,
        file_name=actual_file_name,
        mime="application/pdf",
        use_container_width=True
    )
else:
    st.warning("⚠️ GitHub repository me abhi koi bhi .pdf file nahi mili hai. Kripya pehle file upload karein.")

st.write("---")
st.caption("Developed for Class 9th & 10th Students.")
