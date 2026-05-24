# =========================
# IMPORT LIBRARIES
# =========================

import librosa
import numpy as np

# =========================
# EXTRACT MFCC FEATURES
# =========================

def extract_features(audio, sr):

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=40
    )

    mfcc = np.mean(mfcc.T, axis=0)

    return mfcc