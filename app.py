import streamlit as st

st.set_page_config(page_title="Premium Notes Portal", page_icon="📚", layout="centered")

st.title("🚀 Premium Notes Portal")
st.write("---")

GITHUB_USER = "prabhat-12345"  
REPO_NAME = "notebook"        
FILE_NAME = "DA.PYQ.2025.pdf"  

raw_url = f"https://githubusercontent.com{GITHUB_USER}/{REPO_NAME}/main/{FILE_NAME}"

st.info("🎯 **Class 10 Notes / PYQ Ready Hai!**")
st.write("Neeche diye gaye premium button par click karke PDF ko apne phone me padhein ya download karein.")

st.write("")

# Ekdum clean aur premium button bina kisi screen error ke
st.markdown(f'''
    <a href="{raw_url}" target="_blank" style="text-decoration: none;">
        <div style="
            width: 100%; 
            padding: 15px; 
            background: linear-gradient(135deg, #ff4b4b, #ff7676); 
            color: white; 
            text-align: center; 
            font-size: 18px; 
            font-weight: bold; 
            border-radius: 10px; 
            box-shadow: 0px 4px 10px rgba(255, 75, 75, 0.3);
            cursor: pointer;">
            📖 Open & Download PDF Note
        </div>
    </a>
''', unsafe_allow_html=True)

st.write("---")
st.caption("Developed for Class 9th & 10th Students.")
