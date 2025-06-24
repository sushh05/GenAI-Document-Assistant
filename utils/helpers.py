import streamlit as st
import json
import re
from datetime import datetime
from config.settings import AppConfig

def initialize_session_state():
    """Initialize Streamlit session state variables"""
    if 'document_text' not in st.session_state:
        st.session_state.document_text = ""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'challenge_questions' not in st.session_state:
        st.session_state.challenge_questions = []
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}
    if 'evaluations' not in st.session_state:
        st.session_state.evaluations = {}

def chunk_document(text: str, max_chunk_size: int = AppConfig.MAX_CHUNK_SIZE) -> list:
    """Split document into chunks for better processing"""
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0
    
    for word in words:
        if current_size + len(word) > max_chunk_size and current_chunk:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_size = len(word)
        else:
            current_chunk.append(word)
            current_size += len(word) + 1
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def parse_questions_json(response_text: str) -> list:
    """Parse questions from JSON response"""
    try:
        json_match = re.search(r'\[.*\]', response_text, re.DOTALL)
        
        if json_match:
            questions_json = json_match.group()
            questions = json.loads(questions_json)
            return questions
        else:
            return get_fallback_questions()
    except Exception:
        return get_fallback_questions()

def get_fallback_questions() -> list:
    """Fallback questions if generation fails"""
    return [
        {
            "id": 1,
            "question": "What are the main themes or topics discussed in this document?",
            "type": "Comprehension",
            "difficulty": "Medium",
            "hint": "Look for recurring concepts and main sections"
        },
        {
            "id": 2,
            "question": "How do the different parts of this document relate to each other?",
            "type": "Analysis", 
            "difficulty": "Hard",
            "hint": "Consider cause-effect relationships and logical flow"
        },
        {
            "id": 3,
            "question": "What conclusions can you draw from the information presented?",
            "type": "Synthesis",
            "difficulty": "Medium", 
            "hint": "Think about implications and broader meaning"
        }
    ]

def extract_score_from_evaluation(evaluation_text: str) -> int:
    """Extract numerical score from evaluation text"""
    score_match = re.search(r'Score:\s*(\d+)', evaluation_text)
    if score_match:
        return int(score_match.group(1))
    return 0

def add_to_chat_history(question: str, answer: str):
    """Add Q&A to chat history"""
    st.session_state.chat_history.append({
        'question': question,
        'answer': answer,
        'timestamp': datetime.now().strftime("%H:%M:%S")
    })