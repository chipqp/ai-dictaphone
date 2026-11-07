from faster_whisper import WhisperModel
from typing import Any
from functools import lru_cache


@lru_cache(maxsize=1)
def load_model() -> WhisperModel:
    print("Loading whisper model")
    model_size = "small"
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    return model


def transcribe_audio(audio_path: str) -> dict[str, Any]:
    model = load_model()
    segments, info = model.transcribe(audio_path, beam_size=5)

    segments_list = []

    for segment in segments:
        segments_list.append(
            {
                "start": segment.start,
                "end": segment.end,
                "text": segment.text
            }
        )

    text = "".join(segment["text"] for segment in segments_list).strip()
        
    transcription = {
        "language": info.language,
        "language_probability": info.language_probability,
        "text": text,
        "segments": segments_list
    }

    return transcription


if __name__ == "__main__":
    text = transcribe_audio("app/services/transcription/audio.m4a")
    print(text)