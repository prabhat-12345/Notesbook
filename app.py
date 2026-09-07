import streamlit as st
import os
import urllib.parse

# Premium layout setup
st.set_page_config(page_title="Premium Notes Viewer", page_icon="📚", layout="wide")

st.title("🚀 Premium Notes Portal")
st.write("---")

# 1. Folder se saari .pdf files automatic scan karna
all_files = os.listdir(".")
pdf_files = [f for f in all_files if f.endswith(".pdf")]

if pdf_files:
    pdf_files.sort()
    
    # Dropdown menu ke liye clean naam
    display_names = [f.replace(".pdf", "").replace("_", " ") for f in pdf_files]
    
    selected_display = st.selectbox("📑 Padhne ke liye Chapter chunein:", display_names)
    actual_file_name = pdf_files[display_names.index(selected_display)]
    
    st.write(f"### 📖 Now Reading: {selected_display}")
    
    # Sahi Link Builder (Bina kisi mistake ke)
    GITHUB_USER = "prabhat-12345"
    REPO_NAME = "notebook"
    
    # URL encoded file name taaki spaces se link na toote
    encoded_file_name = urllib.parse.quote(actual_file_name)
    raw_url = f"https://githubusercontent.com{GITHUB_USER}/{REPO_NAME}/main/{encoded_file_name}"
    
    # Google Docs viewer ka bilkul sahi format bina kisi error ke
    google_viewer_url = f"https://google.com{raw_url}&embedded=true"
    
    # 2. DO PREMIUM OPTIONS FOR MOBILE:
    col1, col2 = st.columns(2)
    
    with col1:
        # Option A: Mobile me alag tab me bina download kiye direct open karna (100% Working on Mobile)
        st.markdown(f'''
            <a href="{raw_url}" target="_blank" style="text-decoration: none;">
                <div style="width: 100%; padding: 12px; background: linear-gradient(135deg, #28a745, #5cd65c); color: white; text-align: center; font-size: 16px; font-weight: bold; border-radius: 8px; cursor: pointer; box-shadow: 0px 4px 10px rgba(40, 167, 69, 0.3);">
                    📱 Click Here to Read Full Screen (Mobile)
                </div>
            </a>
        ''', unsafe_allow_html=True)
        
    with col2:
        # Option B: Direct phone storage me download karne ka button
        with open(actual_file_name, "rb") as file:
            pdf_bytes = file.read()
        st.download_button(
            label="📥 Download to Phone Storage",
            data=pdf_bytes,
            file_name=actual_file_name,
            mime="application/pdf",
            use_container_width=True
        )
        
    st.write("")
    st.write("👇 **Neeche App ke andar Preview (Agar white dikhe toh upar 'Mobile View' button dabayein):**")

    # App ke andar ka preview handler
    st.components.v1.html(
        f'<iframe src="{google_viewer_url}" width="100%" height="600px" frameborder="0" style="border: 2px solid #0072ff; border-radius: 10px;"></iframe>', 
        height=620
    )
else:
    st.warning("⚠️ GitHub repository me abhi koi bhi .pdf file nahi mili hai.")

st.write("---")
st.caption("Developed for Class 9th & 10th Students.")
