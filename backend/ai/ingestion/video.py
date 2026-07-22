import ffmpeg
import tempfile

from ai.ingestion.audio import extract_audio_text


def extract_video_text(filepath):

    temp_audio = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    (
        ffmpeg.input(filepath).output(
            temp_audio.name,
            ac=1,
            ar=16000
        ).overwrite_output().run()
    )

    transcript = extract_audio_text(temp_audio.name)

    for item in transcript:
        item["metadata"]["source"] = ("ffmpeg + faster-whisper")

    return transcript