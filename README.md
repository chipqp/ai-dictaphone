# AI Dictaphone

AI Dictaphone is an AI-powered web application for audio transcription and text processing, developed as part of my Bachelor's thesis in Information Technology at Palacký University Olomouc.

The application uses OpenAI's Whisper speech recognition model to convert audio recordings into text, automatically detect spoken languages, and generate timestamped transcription segments.

The project is currently under active development.

## Tech Stack

**Frontend:** React, JavaScript, Vite, HTML, CSS

**Backend:** Python, FastAPI, Pydantic

**Speech Recognition:** faster-whisper (Whisper)

**Tools:** Git, GitHub, uv

## Implemented Features

- Audio file upload (MP3, WAV, M4A)
- Backend file validation (type and size)
- Speech-to-text transcription using faster-whisper
- Automatic language detection
- Full transcription with timestamped segments
- Built-in audio player with clickable timestamps
- Loading states and error handling
- Modular frontend and backend architecture
- REST API communication between React and FastAPI

Speech recognition currently runs locally using the Whisper `small` model on CPU.

## Planned Features

**Audio Processing**
- Audio recording directly from the browser
- Speaker diarization
- Improved handling of longer recordings

**Text Processing**
- Automatic text segmentation and topic detection
- AI-generated summaries
- Keyword extraction

**User Interface**
- Highlighting active transcription segments during playback
- Improved UI and responsive design

**Export & Deployment**
- Transcription export to DOCX and PDF
- Docker-based deployment
- Automated testing and transcription quality evaluation

**Future Development**
- User authentication
- Transcription history and persistent storage
- Background task processing

## Running Locally

### Requirements

- Python 3.14
- [uv](https://docs.astral.sh/uv/)
- Node.js and npm

### Clone the Repository

```bash
git clone https://github.com/chipqp/ai-dictaphone.git
cd ai-dictaphone
```

### Backend

Navigate to the backend directory and install the dependencies:

```bash
cd backend
uv sync
```

Start the FastAPI server:

```bash
uv run uvicorn app.main:app --reload
```

The backend will be available at `http://localhost:8000`.

API documentation: `http://localhost:8000/docs`

### Frontend

Open a second terminal, navigate to the frontend directory and install the dependencies:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173` in your browser.

The frontend communicates with FastAPI through the Vite development proxy.

**Note:** The Whisper model is downloaded automatically on first use. Transcription performance depends on the available hardware.

## API

### POST `/transcriptions/`

Accepts an audio file as `multipart/form-data` using the field name `file`.

The API returns a JSON response containing:

- Detected language
- Language detection confidence
- Full transcription text
- Transcription segments with start and end timestamps

## Project Status

AI Dictaphone is an ongoing Bachelor's thesis project. The current version provides a functional audio transcription workflow with a React frontend and a FastAPI backend.

Further development will focus on text processing, audio recording, export functionality, and deployment.
