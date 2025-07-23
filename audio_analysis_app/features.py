import librosa
import numpy as np

def extract_features(audio_path):
    # Load the audio
    y, sr = librosa.load(audio_path)
    # Extract MFCCs
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    # Estimate tempo (beats per minute)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    if isinstance(tempo, (np.ndarray, list)):
        tempo = float(tempo[0]) if len(tempo) > 0 else 0.0
    # Estimate pitch using the YIN algorithm
    pitch = librosa.yin(y, fmin=50, fmax=300)
    # Output summaries
    print("MFCC shape:", mfccs.shape)
    print("Estimated Tempo (BPM):", tempo)
    print("Pitch Contour (sample):", pitch[:10])
    return y, sr, mfccs, tempo, pitch 