# Audio Analysis Modular App

This app analyzes short-form video audio for emotion, slang, rhythm, and cultural signals using a modular Python pipeline.

## Features

- Extracts audio from video
- Transcribes speech with Whisper
- Analyzes acoustic features (MFCC, tempo, pitch)
- Detects slang and trending phrases
- Measures emotional tone
- Analyzes cadence and delivery style

## Structure

- `main.py`: Orchestrates the pipeline
- `audio_utils.py`: Audio extraction and preprocessing
- `transcription.py`: Whisper transcription
- `features.py`: Acoustic feature extraction
- `emotion.py`: Emotion detection
- `slang.py`: Slang/keyword analysis
- `cadence.py`: Cadence and delivery analysis
- `sample_data/`: Place your video files here

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Place a video file in `sample_data/` (e.g., `your_video.mp4`).
3. Run the app:
   ```
   python main.py sample_data/your_video.mp4
   ```
