import streamlit as st
import os

st.set_page_config(page_title="Premium Notes Portal", page_icon="📚", layout="centered")

st.title("🚀 Premium Notes Portal")
st.write("---")

# Aapki file ka bilkul sahi naam jo repository me hai
FILE_NAME = "DA.PYQ.2025.pdf"  

st.info("🎯 **Class 10 Notes / PYQ Ready Hai!**")
st.write("Neeche diye gaye premium button par click karke PDF ko turant download karein.")
st.write("")

# Bina kisi URL ke seedhe repository se file uthane ka safe tarika
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "rb") as file:
        pdf_bytes = file.read()
        
    # Streamlit ka official trusted button
    st.download_button(
        label="📥 Download PDF Note",
        data=pdf_bytes,
        file_name=FILE_NAME,
        mime="application/pdf",
        use_container_width=True
    )
else:
    st.error(f"⚠️ Repository me '{FILE_NAME}' naam ki file nahi mili! Kripya check karein ki file ka naam GitHub par sahi hai ya nahi.")

st.write("---")
st.caption("Developed for Class 9th & 10th Students.")
