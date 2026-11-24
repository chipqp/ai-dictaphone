# ASR Benchmark

An experimental benchmark for evaluating speech recognition using the Google FLEURS dataset.

- `prepare_dataset.py` — prepares audio samples and reference transcripts.
- `benchmark.py` — runs faster-whisper and saves transcription results.
- `metrics.py` — calculates WER, CER, and RTFx.
- `results/` — contains initial benchmark outputs.

Current baseline: Whisper small on CPU, evaluated on 30 samples. Further model comparisons are planned.
