from pydantic import BaseModel


class TranscriptionSegment(BaseModel):
    start: float
    end: float
    text:str


class TranscriptionResponse(BaseModel):
    language: str
    language_probability: float
    text: str
    segments: list[TranscriptionSegment]