import streamlit as st
from services.gemini_service import GeminiService
from utils.helpers import add_to_chat_history

def render_question_mode():
    """Render question mode interface"""
    st.subheader("Ask About the Document")
    
    user_question = st.text_input(
        "What would you like to know?",
        placeholder="e.g., What are the main findings?"
    )
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("Get Answer"):
            if user_question.strip():
                try:
                    with st.spinner("Finding answer..."):
                        gemini_service = GeminiService()
                        answer = gemini_service.answer_question(
                            user_question, 
                            st.session_state.document_text
                        )
                        
                        add_to_chat_history(user_question, answer)
                        st.write(answer)
                except Exception as e:
                    st.error(f"Error processing question: {e}")
            else:
                st.warning("Please enter a question")
    
    with col2:
        if st.button("Clear History"):
            st.session_state.chat_history = []
            st.success("History cleared")
    
    # Display chat history
    if st.session_state.chat_history:
        st.subheader("Previous Questions")
        with st.expander("Show history"):
            for chat in reversed(st.session_state.chat_history[-5:]):
                st.write(f"**Q:** {chat['question']}")
                st.write(f"**A:** {chat['answer'][:200]}...")
                st.write("---")