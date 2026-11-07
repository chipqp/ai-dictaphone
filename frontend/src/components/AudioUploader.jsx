function AudioUploader({ selectedFile, onFileChange, isLoading, onTranscribe }) {
  return (
    <div>
      
      <input 
        type="file"
        accept=".mp3,.wav,.m4a"
        onChange={onFileChange}
        disabled={isLoading}
      />

      {selectedFile && <p>{selectedFile.name}</p>}

      <button
        disabled={isLoading || !selectedFile}
        onClick={onTranscribe}>
        {isLoading ? "Processing..." : "Transcribe"}
      </button>

    </div>
    )
}

export default AudioUploader