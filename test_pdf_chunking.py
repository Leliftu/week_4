
from src.pdf_processor import extract_text_from_pdf
from src.chunker import chunk_text

# Step 1: Extract text from our PDF
pdf_path = "data/test_document.pdf"

pages = extract_text_from_pdf(pdf_path)

print("PDF extraction completed!")
print("Number of pages:", len(pages))

# Step 2: Divide extracted text into chunks
chunks = chunk_text(
    pages,
    chunk_size=500,
    overlap=100
)

print("\nChunking completed!")
print("Total chunks:", len(chunks))

# Step 3: Display each chunk
for chunk in chunks:
    print("\n------------------------------")
    print("Page:", chunk["page_number"])
    print("Chunk:", chunk["chunk_index"])
    print("Characters:", len(chunk["text"]))
    print("Text:", chunk["text"])
# Step 4: Verify both pages were processed
page_numbers = {chunk["page_number"] for chunk in chunks}

assert page_numbers == {1, 2}, "Not all PDF pages were processed!"

print("\nSUCCESS: Both PDF pages were processed!")