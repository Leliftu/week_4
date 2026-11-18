
# PDF RAG Chatbot

## Project Overview
A PDF-based Question Answering chatbot built using Retrieval-Augmented Generation (RAG).

The application extracts text from PDF documents, divides the text into smaller chunks, generates embeddings, stores them in ChromaDB, retrieves relevant information, and uses Google's Gemini API to generate answers based on the retrieved context.

## Technologies Used
- Python
- PyMuPDF
- Sentence Transformers
- ChromaDB
- Google Gemini API
- python-dotenv

## Features
- PDF text extraction
- Text chunking
- Semantic search
- Vector embedding generation
- Vector storage using ChromaDB
- Context-based answer generation
- Page references for answers

## Project Structure
- `main.py` - Main application
- `src/pdf_processor.py` - PDF text extraction
- `src/text_chunker.py` - Text chunking
- `src/embeddings.py` - Embedding generation
- `src/vector_store.py` - Vector database storage
- `src/retriever.py` - Relevant information retrieval
- `src/llm.py` - Gemini answer generation
- `data/documents/` - Sample PDF

## Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add:

```env
GEMINI_API_KEY=your_api_key
```

5. Run:

```bash
python main.py
```

## Example Question
What is Retrieval-Augmented Generation?

## Expected Output
An answer generated from the PDF with relevant page references.

