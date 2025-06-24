import streamlit as st
from utils.pdf_parser import parse_pdf
from utils.text_parser import parse_txt
from utils.helpers import chunk_document

class DocumentService:
    """Service for document processing operations"""
    
    def process_file(self, uploaded_file):
        """Process uploaded file and extract text"""
        try:
            with st.spinner("Processing document..."):
                if uploaded_file.type == "application/pdf":
                    return parse_pdf(uploaded_file)
                elif uploaded_file.type == "text/plain":
                    return parse_txt(uploaded_file)
                else:
                    st.error("Unsupported file type")
                    return None
        except Exception as e:
            st.error(f"Error processing file: {e}")
            return None
    
    def chunk_document(self, text: str, max_chunk_size: int = None) -> list:
        """Split document into chunks for better processing"""
        if max_chunk_size is None:
            from config.settings import AppConfig
            max_chunk_size = AppConfig.MAX_CHUNK_SIZE
        
        return chunk_document(text, max_chunk_size)