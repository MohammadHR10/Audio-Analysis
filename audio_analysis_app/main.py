from audio_utils import extract_audio
from transcription import transcribe_audio
from features import extract_features
from emotion import estimate_emotion
from slang import extract_bigrams
from cadence import analyze_cadence

# Example usage: python main.py sample_data/your_video.mp4
import sys

def main(video_path):
    print("--- Extracting audio from video ---")
    audio_path = extract_audio(video_path)

    print("--- Transcribing audio ---")
    result = transcribe_audio(audio_path)
    transcript = result["text"]

    print("--- Extracting acoustic features ---")
    y, sr, mfccs, tempo, pitch = extract_features(audio_path)

    print("--- Estimating emotion ---")
    estimate_emotion(pitch, tempo, y)

    print("--- Extracting trending bigrams ---")
    trending, tokens = extract_bigrams(transcript)

    print("--- Analyzing cadence and delivery ---")
    analyze_cadence(y, sr, tokens)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <video_path>")
    else:
        main(sys.argv[1]) 