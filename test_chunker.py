
from src.chunker import chunk_text


def test_chunking():

    pages = [
        {
            "page_number": 1,
            "text": "A" * 1200
        }
    ]

    chunks = chunk_text(
        pages,
        chunk_size=500,
        overlap=100
    )

    assert len(chunks) == 3
    assert len(chunks[0]["text"]) == 500
    assert len(chunks[1]["text"]) == 500
    assert len(chunks[2]["text"]) == 400

    assert chunks[0]["page_number"] == 1

    # Verify that consecutive chunks share 100 characters.
    assert chunks[0]["text"][-100:] == chunks[1]["text"][:100]

    print("All chunking checks passed!")


if __name__ == "__main__":
    test_chunking()
