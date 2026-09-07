import streamlit as st

st.set_page_config(page_title="Premium Notes Portal", page_icon="📚", layout="centered")

st.title("🚀 Premium Notes Portal")
st.write("---")

# Aapki details aur file ka naam
GITHUB_USER = "prabhat-12345"  
REPO_NAME = "notebook"        
FILE_NAME = "DA.PYQ.2025.pdf"  # Jo file aapne upload ki thi

# Direct PDF link bina kisi api ke
raw_url = f"https://githubusercontent.com{GITHUB_USER}/{REPO_NAME}/main/{FILE_NAME}"

st.write(f"### 📑 Reading: Class 10 Notes / PYQ")

# Mobile par PDF dikhane ke liye sabse best viewer
embed_url = f"https://google.com{raw_url}&embedded=true"
st.markdown(f'<iframe src="{embed_url}" width="100%" height="600px" frameborder="0"></iframe>', unsafe_allow_html=True)

st.write("---")
# File download karne ka option
st.markdown(f'<a href="{raw_url}" target="_blank"><button style="width:100%; padding:10px; background-color:#ff4b4b; color:white; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">📥 Open / Download PDF</button></a>', unsafe_allow_html=True)
