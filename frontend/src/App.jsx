import { useState, useRef, useEffect } from 'react'
import './App.css'
import TranscriptionResult from './components/TranscriptionResult'
import AudioUploader from './components/AudioUploader'

function App() {
  const [selectedFile, setSelectedFile] = useState(null)
  const [transcription, setTranscription] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const audioRef = useRef(null)
  const [audioUrl, setAudioUrl] = useState(null)

  function handleSeek(seconds) {
    if (!audioRef.current) return

    audioRef.current.currentTime = seconds
  }

  useEffect(() => {
  if (!selectedFile) {
    setAudioUrl(null)
    return
  }

  const url = URL.createObjectURL(selectedFile)
  setAudioUrl(url)

  return () => {
    URL.revokeObjectURL(url)
  }
}, [selectedFile])

  function handleFileChange(event) {
    const file = event.target.files[0] ?? null
    setSelectedFile(file)
    setTranscription(null)
    setError(null)
  }

  async function handleTranscribe() {
    if (!selectedFile) return

    setError(null)
    setTranscription(null)
    setIsLoading(true)

    const formData = new FormData()
    formData.append("file", selectedFile)

    const request = new Request("/api/transcriptions/", {
      method: "POST",
      body: formData
    })

    try {
      const response = await fetch(request)
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`)
      }
      const result = await response.json()
      setTranscription(result)

    } catch (error) {
      setError(error.message)

    } finally {
      setIsLoading(false)
    }

  }

  return (
    <>
      <section id="center">
        <h1>Audio Transcriptor</h1>

        <AudioUploader
          selectedFile={selectedFile}
          onFileChange={handleFileChange}
          isLoading={isLoading}
          onTranscribe={handleTranscribe}
        />

        {audioUrl && (
          <audio ref={audioRef} controls src={audioUrl}/>
        )}

        {transcription && (
          <TranscriptionResult 
            transcription={transcription}
            onSeek={handleSeek}
          />
        )}

        {error && <p>{error}</p>}
      </section>
    </>
  )
}

export default App
