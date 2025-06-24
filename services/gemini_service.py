import google.generativeai as genai
from config.settings import AppConfig

class GeminiService:
    """Service for interacting with Google Gemini API"""
    
    def __init__(self):
        """Initialize Gemini service"""
        genai.configure(api_key=AppConfig.API_KEY)
        self.model_name = AppConfig.GEMINI_MODEL
    
    def generate_summary(self, document_text: str) -> str:
        """Generate document summary"""
        prompt = f"""
        Please provide a concise summary of the following document in no more than 150 words. 
        Focus on:
        1. Main topic/subject
        2. Key findings or arguments
        3. Important conclusions
        4. Methodology (if applicable)
        
        Document:
        {document_text[:AppConfig.DOCUMENT_PREVIEW_CHARS]}
        """
        
        return self._generate_content(
            prompt,
            temperature=AppConfig.GenerationConfig.SUMMARY_TEMPERATURE,
            max_tokens=AppConfig.GenerationConfig.SUMMARY_MAX_TOKENS
        )
    
    def answer_question(self, question: str, document_text: str) -> str:
        """Answer questions based on document content"""
        prompt = f"""
        You are an assistant that answers questions based ONLY on the provided document content.
        
        IMPORTANT RULES:
        1. Answer ONLY based on information in the document
        2. If the answer is not in the document, clearly state "This information is not available in the provided document"
        3. Always provide justification by referencing specific parts of the document
        4. Include relevant quotes or paraphrases from the document
        5. Be precise and avoid speculation
        
        Document Content:
        {document_text}
        
        Question: {question}
        
        Please provide your answer in this format:
        Answer: [Your answer here]
        
        Justification: [Explain which part of the document supports your answer, include relevant quotes]
        """
        
        return self._generate_content(
            prompt,
            temperature=AppConfig.GenerationConfig.QUESTION_TEMPERATURE,
            max_tokens=AppConfig.GenerationConfig.QUESTION_MAX_TOKENS
        )
    
    def generate_challenge_questions(self, document_text: str) -> str:
        """Generate challenging questions based on document content"""
        prompt = f"""
        Based on the following document, generate exactly 3 challenging questions that test deep understanding:
        
        Question Types to Generate:
        1. COMPREHENSION: Test understanding of main concepts and relationships
        2. ANALYSIS: Require breaking down complex information and identifying patterns
        3. SYNTHESIS: Require combining multiple pieces of information to draw conclusions
        
        Requirements:
        - Questions must be answerable from the document content
        - Each question should require critical thinking, not just factual recall
        - Vary the difficulty levels (medium to hard)
        - Make questions specific to the document's content
        
        Document:
        {document_text[:AppConfig.DOCUMENT_PREVIEW_CHARS]}
        
        Please format your response as a JSON array like this:
        [
            {{
                "id": 1,
                "question": "Your comprehension question here",
                "type": "Comprehension",
                "difficulty": "Medium",
                "hint": "Brief hint if needed"
            }},
            {{
                "id": 2,
                "question": "Your analysis question here", 
                "type": "Analysis",
                "difficulty": "Hard",
                "hint": "Brief hint if needed"
            }},
            {{
                "id": 3,
                "question": "Your synthesis question here",
                "type": "Synthesis", 
                "difficulty": "Medium",
                "hint": "Brief hint if needed"
            }}
        ]
        """
        
        return self._generate_content(
            prompt,
            temperature=AppConfig.GenerationConfig.CHALLENGE_TEMPERATURE,
            max_tokens=AppConfig.GenerationConfig.CHALLENGE_MAX_TOKENS
        )
    
    def evaluate_answer(self, question: str, user_answer: str, document_text: str) -> str:
        """Evaluate user's answer to challenge question"""
        prompt = f"""
        You are evaluating a user's answer to a question based on a document.
        
        Document Content:
        {document_text}
        
        Question: {question}
        User's Answer: {user_answer}
        
        Please evaluate the answer on a scale of 0-10 considering:
        1. Accuracy (Is the answer correct based on the document?)
        2. Completeness (Does it address all parts of the question?)
        3. Evidence (Does it reference relevant parts of the document?)
        4. Understanding (Does it show comprehension of the concepts?)
        
        Provide your evaluation in this format:
        Score: [0-10]
        
        Feedback: [Detailed feedback explaining the score, what was good, what could be improved]
        
        Correct Answer Elements: [What a complete answer should include based on the document]
        
        Document References: [Specific parts of the document that support the correct answer]
        """
        
        return self._generate_content(
            prompt,
            temperature=AppConfig.GenerationConfig.EVALUATION_TEMPERATURE,
            max_tokens=AppConfig.GenerationConfig.EVALUATION_MAX_TOKENS
        )
    
    def _generate_content(self, prompt: str, temperature: float, max_tokens: int) -> str:
        """Generate content using Gemini API"""
        try:
            model = genai.GenerativeModel(
                self.model_name,
                generation_config={
                    "temperature": temperature,
                    "max_output_tokens": max_tokens,
                }
            )
            
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Error generating content: {e}")