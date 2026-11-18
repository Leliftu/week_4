
from src.pdf_processor import extract_text_from_pdf
from src.chunker import chunk_text
from src.embeddings import generate_embeddings
from src.vector_store import store_chunks


def main():

    print("\n===== RAG PROJECT =====")

    # 1. Extract PDF
    print("\n1. Extracting PDF text...")

    pages = extract_text_from_pdf(
        "data/test_document.pdf"
    )

    if not pages:
        print("ERROR: No text found in PDF.")
        return

    print("Pages extracted:", len(pages))

    # 2. Chunk text
    print("\n2. Creating chunks...")

    chunks = chunk_text(
        pages,
        chunk_size=500,
        overlap=100
    )

    print("Chunks created:", len(chunks))

    # 3. Generate embeddings
    print("\n3. Generating embeddings...")

    embedded_chunks = generate_embeddings(chunks)

    print("Embeddings generated:", len(embedded_chunks))

    # 4. Store in ChromaDB
    print("\n4. Storing embeddings...")

    collection = store_chunks(embedded_chunks)

    print("Stored chunks:", collection.count())

    # 5. Verify storage
    print("\n5. Verifying stored documents...")

    results = collection.get(
        include=["documents", "metadatas"]
    )

    for document, metadata in zip(
        results["documents"],
        results["metadatas"]
    ):
        print("\nPage:", metadata["page_number"])
        print("Text:", document[:200])

    assert collection.count() >= len(embedded_chunks)

    print("\nSUCCESS: Module 4 completed!")
    print("Embeddings successfully stored in ChromaDB.")


if __name__ == "__main__":
    main()
