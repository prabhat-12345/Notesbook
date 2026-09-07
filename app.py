import streamlit as st
import os

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
    
    # 2. GitHub se file ka bilkul sahi raw internet link banana embed karne ke liye
    GITHUB_USER = "prabhat-12345"
    REPO_NAME = "notebook"
    raw_url = f"https://githubusercontent.com{GITHUB_USER}/{REPO_NAME}/main/{actual_file_name}"
    
    # 3. Google Docs PDF Viewer (Jo bina download kiye app me hi PDF open karega)
    embed_url = f"https://google.com{raw_url}&embedded=true"
    
    # Premium PDF Box Maker
    st.components.v1.html(
        f'<iframe src="{embed_url}" width="100%" height="700px" frameborder="0" style="border: 2px solid #0072ff; border-radius: 10px;"></iframe>', 
        height=720
    )
    
    st.write("---")
    
    # Safe backup download option niche
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
