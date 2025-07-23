import whisper

def transcribe_audio(audio_path, model_size="base"):
    # Load the Whisper model (you can choose 'tiny', 'base', 'small', etc.)
    model = whisper.load_model(model_size)
    # Transcribe the audio file
    result = model.transcribe(audio_path)
    # Print the raw transcription
    print(result["text"])
    return result 