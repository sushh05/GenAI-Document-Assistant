import streamlit as st
from services.gemini_service import GeminiService

def render_summary_mode():
    """Render summary mode interface"""
    st.subheader("Document Summary")
    
    if st.button("Generate Summary"):
        try:
            with st.spinner("Generating summary..."):
                gemini_service = GeminiService()
                summary = gemini_service.generate_summary(st.session_state.document_text)
                st.write(summary)
        except Exception as e:
            st.error(f"Error generating summary: {e}")