import streamlit as st
import requests

st.set_page_config(page_title="Automatic PDF Notes Portal", page_icon="📚", layout="centered")

st.title("🚀 Premium Notes Portal")
st.write("---")

# Yahan aapki sahi repository details daal di hain
GITHUB_USER = "prabhat-12345"  
REPO_NAME = "notebook"        

def get_all_files():
    api_url = f"https://github.com{GITHUB_USER}/{REPO_NAME}/contents/"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            files = response.json()
            note_files = [f['name'] for f in files if f['name'].endswith(('.pdf', '.txt'))]
            return sorted(note_files)
        return []
    except:
        return []

all_notes = get_all_files()

if all_notes:
    display_names = [name.replace('.pdf', '').replace('.txt', '').replace('_', ' ') for name in all_notes]
    selected_display = st.selectbox("📑 Select Chapter / Note", display_names)
    
    actual_file_name = all_notes[display_names.index(selected_display)]
    raw_url = f"https://githubusercontent.com{GITHUB_USER}/{REPO_NAME}/main/{actual_file_name}"
    
    st.write(f"### 📖 Reading: {selected_display}")
    
    if actual_file_name.endswith('.pdf'):
        embed_url = f"https://google.com{raw_url}&embedded=true"
        st.markdown(f'<iframe src="{embed_url}" width="100%" height="600px" frameborder="0"></iframe>', unsafe_allow_html=True)
    elif actual_file_name.endswith('.txt'):
        text_content = requests.get(raw_url).text
        st.markdown(text_content)
        
    st.write("---")
    st.download_button(label="📥 Download this File", data=raw_url, file_name=actual_file_name)
else:
    st.warning("⚠️ GitHub par abhi koi bhi .pdf ya .txt file nahi mili. Kripya check karein.")
    
