
function formatTime(seconds) {
  const minutes = Math.floor(seconds / 60)
  const remainingSeconds = Math.floor(seconds % 60)

  return (
    String(minutes).padStart(2, '0') + ':' +
    String(remainingSeconds).padStart(2, '0')
  )
}

function TranscriptionResult({ transcription, onSeek }) {
  return (
    <section className="transcription-result">
      <h2>Transcription</h2>
      <p>Detected language: {transcription.language}</p>
      <p>{transcription.text}</p>

      <h3>Segments</h3>

      {transcription.segments.map((segment, index) => (
        <p key={index}>
          <button
            type="button"
            onClick={() => onSeek(segment.start)}
          >
            {formatTime(segment.start)}
          </button>
          {segment.text}
        </p>
      ))}
    </section>
  )
}

export default TranscriptionResult
