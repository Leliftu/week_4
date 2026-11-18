
from src.pdf_processor import extract_text_from_pdf
from src.chunker import chunk_text
from src.embeddings import generate_embeddings


# Extract PDF text
pages = extract_text_from_pdf("data/test_document.pdf")

# Create chunks
chunks = chunk_text(
    pages,
    chunk_size=500,
    overlap=100
)

# Generate embeddings
embedded_chunks = generate_embeddings(chunks)

# Display results
print("\nEmbedding generation completed!")
print("Number of embedded chunks:", len(embedded_chunks))

for chunk in embedded_chunks:
    print("\nPage:", chunk["page_number"])
    print("Embedding dimensions:", len(chunk["embedding"]))
    print("First 5 vector values:", chunk["embedding"][:5])

# Verify the embedding dimensions
assert all(
    len(chunk["embedding"]) == 384
    for chunk in embedded_chunks
)

print("\nSUCCESS: All embeddings have 384 dimensions!")
