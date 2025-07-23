import streamlit as st
import os
from audio_utils import extract_audio
from transcription import transcribe_audio
from features import extract_features
from emotion import estimate_emotion
from slang import extract_bigrams
from cadence import analyze_cadence

st.title("Audio Analysis App")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])
if uploaded_file:
    save_path = os.path.join(os.getcwd(), "temp_video.mp4")
    with open(save_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"Video uploaded and saved to {save_path}")
    st.write("File exists:", os.path.exists(save_path))
    st.write("File size:", os.path.getsize(save_path) if os.path.exists(save_path) else 0)

    if st.button("Run Analysis"):
        from moviepy.editor import VideoFileClip
        video = VideoFileClip(save_path)
        if video.audio is None:
            st.error("No audio track found in the uploaded video.")
            st.stop()
        audio_path = extract_audio(save_path)
        result = transcribe_audio(audio_path)
        transcript = result["text"]
        st.subheader("Transcript")
        st.write(transcript)

        y, sr, mfccs, tempo, pitch = extract_features(audio_path)
        emotion = estimate_emotion(pitch, tempo, y)
        st.subheader("Estimated Emotion")
        st.write(emotion)

        trending, tokens = extract_bigrams(transcript)
        st.subheader("Trending Bigrams")
        st.write(trending)

        wps, filler_ratio, filler_count = analyze_cadence(y, sr, tokens)
        st.subheader("Cadence")
        st.write(f"Words per second: {wps:.2f}, Filler ratio: {filler_ratio:.3f}")