from datasets import load_dataset
from itertools import islice
from pathlib import Path
import json


DATA_DIR = Path(__file__).resolve().parent / "data" / "cs"
AUDIO_DIR = DATA_DIR / "audio"
AUDIO_AMOUNT = 30

AUDIO_DIR.mkdir(parents=True, exist_ok=True)

dataset = load_dataset("google/fleurs", "cs_cz", split="test", streaming=True)
dataset = dataset.decode(False)

transcription_path = DATA_DIR / "references.jsonl"

with transcription_path.open("w", encoding="utf-8") as jsonl_file:
    for sample in islice(dataset, AUDIO_AMOUNT):
        audio_bytes = sample["audio"]["bytes"]
        audio_path = AUDIO_DIR / f"{sample['id']}.wav"
        audio_path.write_bytes(audio_bytes)

        record = {
            "id": sample["id"],
            "audio": audio_path.relative_to(DATA_DIR).as_posix(),
            "text": sample["transcription"],
            "language": sample["language"]
            }

        jsonl_file.write(json.dumps(record, ensure_ascii=False) + '\n')
