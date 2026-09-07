import streamlit as st
import requests

st.set_page_config(page_title="Premium Notes Portal", page_icon="📚", layout="centered")

st.title("🚀 Premium Notes Portal (100% Automatic)")
st.write("---")

# 🔴 APNI REPO DETAILS YAHAN SET HAI 🔴
GITHUB_USER = "prabhat-12345"  
REPO_NAME = "notebook"        

@st.cache_data(ttl=60)  # Har 60 second me automatically naya data check karega
def get_pdf_files_auto():
    # GitHub API se bina kisi link error ke data nikalne ka tareeka
    api_url = f"https://github.com{GITHUB_USER}/{REPO_NAME}/contents/"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            files_list = response.json()
            # Sirf aur sirf .pdf files ko apne aap khinchega
            pdfs = [f['name'] for f in files_list if f['name'].endswith('.pdf')]
            return pdfs
        return []
    except:
        return []

# Pura data automatic khinch kar aa gaya
pdf_files = get_pdf_files_auto()

if pdf_files:
    pdf_files.sort()
    
    # Dropdown menu me clean naam dikhane ke liye
    clean_names = [f.replace(".pdf", "").replace("_", " ") for f in pdf_files]
    
    selected_name = st.selectbox("📑 Select Note / PYQ", clean_names)
    
    # Asli file ka naam select karna
    actual_file = pdf_files[clean_names.index(selected_name)]
    
    # Download karne ke liye direct raw internet link
    raw_download_url = f"https://githubusercontent.com{GITHUB_USER}/{REPO_NAME}/main/{actual_file}"
    
    st.success(f"🎯 **{selected_name}** padhne ke liye taiyar hai!")
    st.write("")
    
    # Pura optimized premium button jo direct click pe download shuru karega
    st.markdown(f'''
        <a href="{raw_download_url}" download target="_blank" style="text-decoration: none;">
            <div style="
                width: 100%; 
                padding: 15px; 
                background: linear-gradient(135deg, #00c6ff, #0072ff); 
                color: white; 
                text-align: center; 
                font-size: 18px; 
                font-weight: bold; 
                border-radius: 10px; 
                box-shadow: 0px 4px 15px rgba(0, 114, 255, 0.4);
                cursor: pointer;">
                📥 Click to Download / Open PDF
            </div>
        </a>
    ''', unsafe_allow_html=True)

else:
    st.warning("⚠️ GitHub par koi .pdf file nahi mili. Ek baar check karein ya naya file upload karein.")

st.write("---")
st.caption("Developed for Class 9th & 10th Students.")
