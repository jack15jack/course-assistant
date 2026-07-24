from functools import lru_cache

@lru_cache(maxsize=1)
def get_whisper_model():

    from faster_whisper import WhisperModel

    return WhisperModel(
        "base",
        device="cpu",
        compute_type="int8"
    )

def extract_audio_text(filepath):

    model = get_whisper_model()

    segments, info = model.transcribe(
        filepath,
        beam_size=5
    )

    text = []

    metadata = {
        "source": "faster-whisper",
        "language": info.language,
        "segments": []
    }

    for segment in segments:

        text.append(segment.text)

        metadata["segments"].append(
            {
                "start": segment.start,
                "end": segment.end
            }
        )

    return [
        {
            "content_type": "transcript",
            "content": " ".join(text),
            "metadata": metadata
        }
    ]