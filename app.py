import streamlit as st
import requests

st.set_page_config(page_title="Automatic PDF Notes Portal", page_icon="📚", layout="centered")

st.title("🚀 Premium Notes Portal (Auto-Update)")
st.write("---")

# 🔴 APNI DETAILS YAHAN BHAREIN 🔴
GITHUB_USER = "Aapka_GitHub_Username"  # Apna asli GitHub Username likhein
REPO_NAME = "notes-app"                # Apni repository ka naam

# Function: Jo GitHub se saari files ki list automatically nikalega
def get_all_files():
    api_url = f"https://github.com{GITHUB_USER}/{REPO_NAME}/contents/"
    response = requests.get(api_url)
    if response.status_code == 200:
        files = response.json()
        # Sirf un files ko chunna jinke aakhiri me .pdf ya .txt aata hai
        note_files = [f['name'] for f in files if f['name'].endswith(('.pdf', '.txt'))]
        return sorted(note_files)
    else:
        return []

# Background me saari files automatic load ho jayengi
all_notes = get_all_files()

if all_notes:
    # Student ke samne automatic dropdown list aa jayegi
    # File ke naam se '.pdf' ya '.txt' hata kar saaf naam dikhane ke liye
    display_names = [name.replace('.pdf', '').replace('.txt', '').replace('_', ' ') for name in all_notes]
    
    selected_display = st.selectbox("📑 Select Chapter / Note", display_names)
    
    # Asli file ka naam nikalna link banane ke liye
    actual_file_name = all_notes[display_names.index(selected_display)]
    
    # Raw Link automatic generate ho jayega
    raw_url = f"https://githubusercontent.com{GITHUB_USER}/{REPO_NAME}/main/{actual_file_name}"
    
    st.write(f"### 📖 Reading: {selected_display}")
    
    # Agar PDF file hai toh screen par embed karein
    if actual_file_name.endswith('.pdf'):
        # Google Docs viewer ka use mobile par PDF ko best tarike se load karne ke liye
        embed_url = f"https://google.com{raw_url}&embedded=true"
        st.markdown(f'<iframe src="{embed_url}" width="100%" height="600px" frameborder="0"></iframe>', unsafe_allow_html=True)
    
    # Agar Text file hai toh direct text dikhayein
    elif actual_file_name.endswith('.txt'):
        text_content = requests.get(raw_url).text
        st.markdown(text_content)
        
    st.write("---")
    # Download Button bhi automatic ban jayega
    st.download_button(label="📥 Download this File", data=raw_url, file_name=actual_file_name)

else:
    st.warning("⚠️ GitHub par abhi tak koi bhi .pdf ya .txt notes file upload nahi ki gayi hai.")
  
