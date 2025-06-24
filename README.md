# Document Assistant

## Project Description

This project is a Streamlit-based web application that helps users interact with their documents in three primary ways: summarizing content, asking questions, and challenging their understanding through comprehension tests. It leverages the Google Gemini API for advanced natural language processing capabilities.

## Features

- **Document Upload**: Supports PDF and  text (.txt) file uploads.
- **Document Summarization**: Generates concise summaries of uploaded documents using the Gemini API.
- **Question Answering**: Allows users to ask specific questions about the document content and receive answers based solely on the provided text.
- **Memory Handling**: Supports follow-up questions that refer to prior interactions to maintain context.


- **Answer Highlighting**: Displays the specific snippet from the source document that supports each answer.


- **Challenge Mode**: Generates challenging comprehension questions (Comprehension, Analysis, Synthesis) based on the document, and evaluates user answers.
- **Intuitive User Interface**: Built with Streamlit for an easy-to-use and interactive experience.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyMuPDF (for PDF parsing)
- python-dotenv

## Setup and Installation

### Prerequisites

- Python 3.8+
- Google Gemini API Key

### Steps

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Google Gemini API Key:**

   Create a `.env` file in the root directory of the project and add your Gemini API key:

   ```
   GOOGLE_API_KEY='YOUR_GEMINI_API_KEY'
   ```

   Replace `YOUR_GEMINI_API_KEY` with your actual API key obtained from the Google AI Studio.

## Usage

1. **Run the Streamlit application:**

   ```bash
   streamlit run app.py
   ```

2. **Access the application:**

   Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. **Upload a document:**

   Use the sidebar to upload a PDF or TXT file.

4. **Choose a mode:**

   Select one of the following modes from the dropdown menu:
   - **Summary**: Click 'Generate Summary' to get a concise overview of your document.
   - **Ask Questions**: Type your question in the input field and click 'Get Answer' to receive information based on the document.
   - **Challenge Me**: Click 'Generate Questions' to get comprehension questions. Type your answers and click 'Submit Answer' to get an evaluation.

## Project Structure

```
.env
app.py
requirements.txt
config/
    settings.py
services/
    document_service.py
    gemini_service.py
ui/
    challenge_mode.py
    question_mode.py
    sidebar.py
    summary_mode.py
utils/
    helpers.py
    pdf_parser.py
    text_parser.py
```

- `app.py`: The main Streamlit application file.
- `requirements.txt`: Lists all Python dependencies.
- `config/settings.py`: Contains application-wide configuration settings, including API keys and generation parameters.
- `services/document_service.py`: Handles document processing, including file parsing and text extraction.
- `services/gemini_service.py`: Manages interactions with the Google Gemini API for summarization, question answering, and question generation/evaluation.
- `ui/`: Contains Streamlit UI components for different modes of interaction.
    - `challenge_mode.py`: UI and logic for the 'Challenge Me' mode.
    - `question_mode.py`: UI and logic for the 'Ask Questions' mode.
    - `sidebar.py`: UI and logic for the application sidebar, including file upload.
    - `summary_mode.py`: UI and logic for the 'Summary' mode.
- `utils/`: Contains utility functions.
    - `helpers.py`: General utility functions, including session state management, document chunking, and JSON parsing.
    - `pdf_parser.py`: Handles parsing of PDF files.
    - `text_parser.py`: Handles parsing of plain text files.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details (if applicable).

## Contact

For any questions or feedback, please open an issue on GitHub.


