from fastapi import UploadFile, APIRouter
from app.services.audio_validation import validate_audio_file
from tempfile import TemporaryDirectory
from pathlib import Path
from starlette.concurrency import run_in_threadpool
from app.services.transcription.whisper_service import transcribe_audio
from app.schemas.transcription import TranscriptionResponse


CHUNK_SIZE = 1024 * 1024

router = APIRouter(prefix="/transcriptions")

@router.post("/", response_model=TranscriptionResponse)
async def create_transcription(file: UploadFile):
    await validate_audio_file(file)

    extension = Path(file.filename or "").suffix.lower()

    with TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / f"audio{extension}"

        with open(temp_path, "wb") as tmp_file:
            while True:
                chunk = await file.read(CHUNK_SIZE)
                if not chunk:
                    break
                tmp_file.write(chunk)

        result = await run_in_threadpool(
            transcribe_audio,
            str(temp_path)
        )

    return result
