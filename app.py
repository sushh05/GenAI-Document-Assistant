from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

from config.settings import AppConfig
from services.document_service import DocumentService
from ui.sidebar import render_sidebar
from ui.summary_mode import render_summary_mode
from ui.question_mode import render_question_mode
from ui.challenge_mode import render_challenge_mode
from utils.helpers import initialize_session_state

def main():
    """Main application function"""
    # Configure Streamlit
    st.set_page_config(
        page_title=AppConfig.APP_TITLE,
        layout="wide"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # App header
    st.title(AppConfig.APP_TITLE)
    st.write(AppConfig.APP_DESCRIPTION)
    
    # Render sidebar and get uploaded file
    uploaded_file = render_sidebar()
    
    # Process uploaded file
    if uploaded_file:
        document_service = DocumentService()
        document_text = document_service.process_file(uploaded_file)
        
        if document_text:
            st.session_state.document_text = document_text
            st.success(f"Document processed successfully. Length: {len(document_text):,} characters")
        else:
            st.error("Failed to extract text from document")
    
    # Main interface
    if st.session_state.document_text:
        render_main_interface()
    else:
        render_welcome_screen()

def render_main_interface():
    """Render the main interface with mode selection"""
    st.subheader("Choose what you'd like to do")
    mode = st.selectbox(
        "Select an option:",
        ["Summary", "Ask Questions", "Challenge Me"],
        key="mode_selector"
    )
    
    if mode == "Summary":
        render_summary_mode()
    elif mode == "Ask Questions":
        render_question_mode()
    elif mode == "Challenge Me":
        render_challenge_mode()

def render_welcome_screen():
    """Render welcome screen when no document is uploaded"""
    st.subheader("Welcome")
    st.write("""
    This tool helps you work with your documents in three ways:
    
    **Summary** - Get a quick overview of the main points
    
    **Ask Questions** - Get answers about specific topics in your document
    
    **Challenge Me** - Answer questions to check how well you understand the content
    
    To get started, upload a PDF or text file using the sidebar.
    """)
    
    st.write("**Example questions you can ask:**")
    st.write("- What are the main findings?")
    st.write("- How does the methodology work?")
    st.write("- What are the key conclusions?")
    st.write("- What evidence supports the main points?")

if __name__ == "__main__":
    main()