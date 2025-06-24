import streamlit as st
from config.settings import AppConfig

def render_sidebar():
    """Render sidebar with file upload"""
    with st.sidebar:
        st.subheader("Upload Document")
        uploaded_file = st.file_uploader(
            "Choose a PDF or TXT file", 
            type=AppConfig.SUPPORTED_FILE_TYPES
        )
        
        if uploaded_file:
            st.write("File uploaded successfully")
            st.write(f"Filename: {uploaded_file.name}")
            st.write(f"Size: {uploaded_file.size:,} bytes")
    
    return uploaded_file