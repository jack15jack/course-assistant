from faster_whisper import WhisperModel

model = WhisperModel(
    "base",
    device="auto",
    compute_type="int8"
)

def extract_audio_text(filepath):

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

                "content_metadata":
                {
                    "start":segment.start,
                    "end":segment.end,
                    "language":info.language,
                    "source":"faster-whisper"
                }
            }
        )

    return results