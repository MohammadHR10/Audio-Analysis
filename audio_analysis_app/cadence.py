import librosa

def analyze_cadence(y, sr, tokens):
    # Estimate total audio duration in seconds
    duration_sec = librosa.get_duration(y=y, sr=sr)
    # Count total words
    words = len(tokens)
    # Compute words per second (speech rate)
    wps = words / duration_sec
    print(f"Words per second (WPS): {wps:.2f}")
    # Optional: Detect filler words (basic example set)
    filler_words = {'um', 'uh', 'like', 'you know', 'so', 'actually'}
    filler_count = sum(token in filler_words for token in tokens)
    filler_ratio = filler_count / words if words > 0 else 0
    print(f"Filler word ratio: {filler_ratio:.3f} ({filler_count} fillers in {words} words)")
    return wps, filler_ratio, filler_count 