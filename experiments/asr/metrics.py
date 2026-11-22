import json
from pathlib import Path
import re
from jiwer import wer, cer
from config import RESULTS_DIR, DATA_DIR
import soundfile as sf


# https://huggingface.co/learn/audio-course/en/chapter5/evaluation


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[\W_]+", " ", text)
    text = text.strip()

    return text


def load_results(file_path: Path) -> list[dict]:
    results = []
    with file_path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            record = json.loads(line)
            results.append(record)
    return results


def evaluate_results(results: list[dict]) -> dict[str, float]:
    references = [normalize_text(record["reference"]) for record in results]
    predictions = [normalize_text(record["prediction"]) for record in results]
    word_error = wer(references, predictions)
    char_error = cer(references, predictions)

    return {
        "wer": word_error,
        "cer": char_error
    }


def get_audio_duration(audio_path: Path) -> float:
    audio_info = sf.info(audio_path)
    return audio_info.duration


def calculate_rtfx(results: list[dict], data_dir: Path) -> float:
    total_audio_duration = 0
    total_processing_time = 0

    for record in results:
        audio_path = data_dir / "audio" / f"{record['id']}.wav"
        audio_duration = get_audio_duration(audio_path)
        total_audio_duration += audio_duration
        total_processing_time += record["processing_time"]

    rtfx = total_audio_duration / total_processing_time
    
    return rtfx


if __name__ == "__main__":
    results_path = RESULTS_DIR / "cs_small.jsonl"

    results = load_results(results_path)
    metrics = evaluate_results(results)

    print(f"Samples: {len(results)}")
    print(f"WER: {metrics['wer']:.2%}")
    print(f"CER: {metrics['cer']:.2%}")

    rtfx = calculate_rtfx(results, DATA_DIR)
    print(f"RTFx: {rtfx:.2f}x")



# learn Inverse Real-Time Factor (RTFx) ???