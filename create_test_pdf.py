
import pymupdf

# Create a new PDF document
doc = pymupdf.open()

# Create page 1
page1 = doc.new_page()
page1.insert_text(
    (72, 72),
    "Introduction to Artificial Intelligence\n\n"
    "Artificial Intelligence enables computers "
    "to perform tasks that normally require human intelligence."
)

# Create page 2
page2 = doc.new_page()
page2.insert_text(
    (72, 72),
    "Introduction to RAG\n\n"
    "Retrieval-Augmented Generation combines "
    "information retrieval with large language models."
)

# Save the PDF
doc.save("data/test_document.pdf")
doc.close()

print("Test PDF created successfully!")
