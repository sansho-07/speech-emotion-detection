# =========================
# IMPORT LIBRARIES
# =========================

import streamlit as st
import os
import sys
from pathlib import Path

# Ensure the repository root is on Python path so `src` imports work from Streamlit.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.prediction import predict_emotion

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Speech Emotion Recognition",
    page_icon="🎤",
    layout="centered"
)

# =========================
# TITLE
# =========================

st.title("🎤 Speech Emotion Recognition AI")

st.markdown("""
This AI system predicts human emotions from speech audio using:
- Deep Learning
- CNN Architecture
- MFCC Audio Features
""")

# =========================
# SIDEBAR
# =========================

st.sidebar.header("About Project")

st.sidebar.info("""
Developed using:
- TensorFlow
- Librosa
- Streamlit
- Deep Learning
""")

# =========================
# FILE UPLOADER
# =========================

uploaded_file = st.file_uploader(
    "Upload WAV Audio File",
    type=["wav"]
)

# =========================
# PREDICTION
# =========================

if uploaded_file is not None:

    temp_path = "temp_audio.wav"

    with open(temp_path, "wb") as f:

        f.write(uploaded_file.read())

    # Audio Player
    st.audio(temp_path)

    # Predict Button
    if st.button("Predict Emotion"):

        with st.spinner("Analyzing Emotion..."):

            emotion, confidence = predict_emotion(
                temp_path
            )

        st.success(
            f"Predicted Emotion: {emotion}"
        )

        st.info(
            f"Confidence Score: {confidence:.2f}"
        )

    # Cleanup
    os.remove(temp_path)