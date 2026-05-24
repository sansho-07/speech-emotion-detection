import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

# =========================
# IMPORT LIBRARIES
# =========================

import streamlit as st
import os

from src.prediction import predict_emotion

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Speech Emotion Recognition",
    layout="centered"
)

# =========================
# TITLE
# =========================

st.title("🎤 Speech Emotion Recognition")

st.write(
    "Upload a speech audio file to detect emotion."
)

# =========================
# FILE UPLOAD
# =========================

uploaded_file = st.file_uploader(
    "Upload WAV File",
    type=["wav"]
)

# =========================
# PREDICTION
# =========================

if uploaded_file is not None:

    temp_path = "temp_audio.wav"

    with open(temp_path, "wb") as f:

        f.write(uploaded_file.read())

    st.audio(temp_path)

    # Predict emotion
    emotion, confidence = predict_emotion(temp_path)

    # Display results
    st.success(f"Predicted Emotion: {emotion}")

    st.info(f"Confidence: {confidence:.2f}")

    # Remove temp file
    os.remove(temp_path)