import numpy as np

def estimate_emotion(pitch, tempo, y):
    # Compute basic stats
    pitch_mean = np.mean(pitch)
    pitch_std = np.std(pitch)
    volume = np.sqrt(np.mean(y**2))  # RMS energy
    # Basic heuristics for emotion classification
    if pitch_std > 30 and tempo > 100 and volume > 0.02:
        emotion = "Excited / Happy"
    elif pitch_std < 10 and tempo < 80:
        emotion = "Calm / Sad"
    elif pitch_std > 20 and tempo > 90:
        emotion = "Energetic / Angry"
    else:
        emotion = "Neutral or Uncertain"
    print("Estimated Emotion Tone:", emotion)
    print("DEBUG:", pitch_std, tempo, volume)
    print(f"Pitch Std Dev: {pitch_std:.2f} | Tempo: {tempo:.2f} | Volume (RMS): {volume:.4f}")
    return emotion 