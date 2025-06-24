import streamlit as st
from services.gemini_service import GeminiService
from utils.helpers import parse_questions_json, extract_score_from_evaluation

def render_challenge_mode():
    """Render challenge mode interface"""
    st.subheader("Challenge Me")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("Generate Questions"):
            try:
                with st.spinner("Creating questions..."):
                    gemini_service = GeminiService()
                    response = gemini_service.generate_challenge_questions(
                        st.session_state.document_text
                    )
                    st.session_state.challenge_questions = parse_questions_json(response)
                    st.session_state.user_answers = {}
                    st.session_state.evaluations = {}
                    st.success("Questions generated")
            except Exception as e:
                st.error(f"Error generating questions: {e}")
    
    with col2:
        if st.session_state.challenge_questions:
            if st.button("New Questions"):
                st.session_state.challenge_questions = []
                st.session_state.user_answers = {}
                st.session_state.evaluations = {}
                st.rerun()
    
    # Display questions
    if st.session_state.challenge_questions:
        render_challenge_questions()
    else:
        st.write("Click 'Generate Questions' to start the challenge.")

def render_challenge_questions():
    """Render the challenge questions interface"""
    st.write("Answer the following questions based on the document:")
    
    for i, question_data in enumerate(st.session_state.challenge_questions):
        st.write(f"**Question {i+1}** ({question_data['type']} - {question_data['difficulty']})")
        st.write(question_data['question'])
        
        if 'hint' in question_data:
            st.write(f"*Hint: {question_data['hint']}*")
        
        # Answer input
        user_answer = st.text_area(
            "Your answer:",
            key=f"answer_{i}",
            height=100
        )
        
        # Submit answer
        if st.button(f"Submit Answer {i+1}", key=f"submit_{i}"):
            if user_answer.strip():
                try:
                    st.session_state.user_answers[i] = user_answer
                    
                    with st.spinner("Evaluating answer..."):
                        gemini_service = GeminiService()
                        evaluation = gemini_service.evaluate_answer(
                            question_data['question'], 
                            user_answer, 
                            st.session_state.document_text
                        )
                        st.session_state.evaluations[i] = evaluation
                except Exception as e:
                    st.error(f"Error evaluating answer: {e}")
            else:
                st.warning("Please provide an answer")
        
        # Show evaluation if available
        if i in st.session_state.evaluations:
            render_evaluation(i)
        
        st.write("---")
    
    # Progress
    if st.session_state.evaluations:
        answered = len(st.session_state.evaluations)
        total = len(st.session_state.challenge_questions)
        st.write(f"Progress: {answered}/{total} questions answered")

def render_evaluation(question_index: int):
    """Render evaluation for a specific question"""
    st.write("**Evaluation:**")
    evaluation_text = st.session_state.evaluations[question_index]
    
    score = extract_score_from_evaluation(evaluation_text)
    if score >= 8:
        st.success(f"Score: {score}/10")
    elif score >= 6:
        st.info(f"Score: {score}/10")
    elif score >= 4:
        st.warning(f"Score: {score}/10")
    else:
        st.error(f"Score: {score}/10")
    
    st.write(evaluation_text)