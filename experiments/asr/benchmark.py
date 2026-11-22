from pathlib import Path
import json
from faster_whisper import WhisperModel
import time
from config import DATA_DIR, RESULTS_DIR


def load_samples(data_dir: Path ) -> list[dict]:
    references_path = data_dir / "references.jsonl"
    data = []

    with references_path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            record = json.loads(line)
            data.append(record)
    return data


def transcribe_sample(model: WhisperModel, audio_path: Path) -> tuple[str, float]:
    start = time.perf_counter()

    segments, _ = model.transcribe(
        str(audio_path),
        beam_size=5,
        language="cs"
    )

    text = "".join(segment.text for segment in segments).strip()
    end = time.perf_counter()
    total_time = end - start

    return text, total_time


def run_benchmark(model: WhisperModel, model_name: str, samples: list[dict], data_dir: Path) -> list[dict]:
    results = []

    for sample in samples:
        audio_path = data_dir / sample["audio"]
        text, total_time = transcribe_sample(model, audio_path)
        result = {
            "id": sample["id"],
            "model": model_name,
            "reference": sample["text"],
            "prediction": text,
            "processing_time": total_time
        }
        results.append(result)

    return results


def save_results(results: list[dict], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open(mode="w", encoding="utf-8") as file:
        for record in results:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")
    return


if __name__ == "__main__":
    samples = load_samples(DATA_DIR)
    model = WhisperModel("small", device="cpu", compute_type="int8")

    results = run_benchmark(model, "small", samples, DATA_DIR)
    total_processing_time = sum(result["processing_time"] for result in results)

    print(f"Processed: {len(results)}")
    print(f"Total processing time: {total_processing_time:.2f} s")
    print(f"Average processing time: {total_processing_time / len(results):.2f} s")

    output_path = RESULTS_DIR / "cs_small.jsonl"
    save_results(results, output_path)

