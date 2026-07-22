from functools import lru_cache

@lru_cache(maxsize=1)
def get_whisper_model():

    from faster_whisper import WhisperModel

    return WhisperModel(
        "base",
        device="auto",
        compute_type="int8"
    )

def extract_audio_text(filepath):

    model = get_whisper_model()

    segments, info = model.transcribe(
        filepath,
        beam_size=5
    )

    results = []

    for segment in segments:
        results.append(
            {
                "content_type":"transcript",

                "content":segment.text,

                "metadata":
                {
                    "start":segment.start,
                    "end":segment.end,
                    "language":info.language,
                    "source":"faster-whisper"
                }
            }
        )

    return results