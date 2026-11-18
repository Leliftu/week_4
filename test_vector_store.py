
from src.pdf_processor import extract_text_from_pdf
from src.chunker import chunk_text
from src.embeddings import generate_embeddings
from src.vector_store import store_chunks


# 1. Extract PDF text
pages = extract_text_from_pdf("data/test_document.pdf")

# 2. Create chunks
chunks = chunk_text(
    pages,
    chunk_size=500,
    overlap=100
)

# 3. Generate embeddings
embedded_chunks = generate_embeddings(chunks)

# 4. Store everything in ChromaDB
collection = store_chunks(embedded_chunks)

# 5. Verify storage
print("\nChromaDB storage completed!")

print("Stored chunks:", collection.count())

# 6. Retrieve stored records
results = collection.get(
    include=["documents", "metadatas"]
)

for document, metadata in zip(
    results["documents"],
    results["metadatas"]
):
    print("\nPage:", metadata["page_number"])
    print("Text:", document)

assert collection.count() >= len(embedded_chunks)

print("\nSUCCESS: Embeddings stored in ChromaDB!")
