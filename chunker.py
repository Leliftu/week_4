
def chunk_text(pages, chunk_size=500, overlap=100):
    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk_size.")

    chunks = []
    step = chunk_size - overlap

    for page in pages:
        text = page["text"]
        page_number = page["page_number"]

        for start in range(0, len(text), step):
            chunk = text[start:start + chunk_size]

            if chunk.strip():
                chunks.append({
                    "text": chunk,
                    "page_number": page_number
                })

    return chunks
