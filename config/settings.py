import os

class AppConfig:
    """Application configuration settings"""
    APP_TITLE = "Document Assistant"
    APP_DESCRIPTION = "Upload a document and analyze it through summaries, questions, or comprehension tests."
    
    # File settings
    SUPPORTED_FILE_TYPES = ['pdf', 'txt']
    MAX_CHUNK_SIZE = 3000
    DOCUMENT_PREVIEW_CHARS = 4000
    
    # Gemini settings
    GEMINI_MODEL = 'gemini-2.0-flash-exp'
    API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # Generation settings
    class GenerationConfig:
        SUMMARY_TEMPERATURE = 0.3
        SUMMARY_MAX_TOKENS = 200
        
        QUESTION_TEMPERATURE = 0.2
        QUESTION_MAX_TOKENS = 500
        
        CHALLENGE_TEMPERATURE = 0.5
        CHALLENGE_MAX_TOKENS = 800
        
        EVALUATION_TEMPERATURE = 0.3
        EVALUATION_MAX_TOKENS = 600