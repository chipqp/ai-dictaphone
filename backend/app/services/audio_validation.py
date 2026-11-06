from fastapi import UploadFile, HTTPException
from pathlib import Path

ALLOWED_EXTENSIONS = {".mp3", ".m4a", ".wav"} # Bad validation for test porp only
MAX_FILE_SIZE = 25 * 1024 * 1024
CHUNK_SIZE = 1024 * 1024
ALLOWED_MIME_TYPES = {
    "audio/mpeg",
    "audio/wav",
    "audio/x-wav",
    "audio/mp4",
    "audio/x-m4a"
}

async def validate_audio_file(file: UploadFile):
    """Validate audio file type and size"""
    
    # Replace this file type validation! 
    extension = Path(file.filename or "").suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file extension"
        )
    
    file_mime_type = file.content_type
    if file_mime_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsopported file type"
        )

    # File size test
    total_size = 0
    while True:
        chunk = await file.read(CHUNK_SIZE)
        if not chunk:
            break

        total_size += len(chunk)

        if total_size > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=413,
                detail="File is too big"
            )

    if total_size == 0:
        raise HTTPException(
            status_code=400,
            detail="File is empty"
        )

    await file.seek(0)