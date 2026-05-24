# =========================
# IMPORT LIBRARIES
# =========================

import librosa
import numpy as np

# =========================
# PREPROCESS AUDIO
# =========================

def preprocess_audio(audio_path, duration=3):

    audio, sr = librosa.load(audio_path)

    # Remove silence
    audio, _ = librosa.effects.trim(audio)

    # Normalize
    audio = librosa.util.normalize(audio)

    # Standardize length
    target_length = sr * duration

    if len(audio) > target_length:

        audio = audio[:target_length]

    else:

        padding = target_length - len(audio)

        audio = np.pad(audio, (0, padding))

    return audio, sr