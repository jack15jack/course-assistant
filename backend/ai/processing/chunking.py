def chunk_text(
    text,
    chunk_size=1500,
    overlap=200
):

    chunks = []
    start = 0
    length = len(text)

    while start < length:

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(
            {
                "content": chunk.strip(),
                "chunk_index": len(chunks),
                "metadata": {
                    "start": start,
                    "end": end
                }
            }
        )

        start = end - overlap

    return chunks