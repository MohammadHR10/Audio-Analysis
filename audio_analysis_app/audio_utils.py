from moviepy.editor import VideoFileClip
import librosa
import numpy as np


def extract_audio(video_path, output_path='audio.wav'):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(output_path, codec='pcm_s16le')
    return output_path


def load_and_preprocess(audio_path, sr=16000):
    # Load audio, convert to mono, resample, normalize
    y, orig_sr = librosa.load(audio_path, sr=None, mono=True)
    if orig_sr != sr:
        y = librosa.resample(y, orig_sr, sr)
    y = y / np.max(np.abs(y))  # Normalize
    return y, sr 