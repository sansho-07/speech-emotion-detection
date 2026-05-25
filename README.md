---
title: Speech Emotion Recognition
emoji: 🎤
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# Speech Emotion Recognition

[![Hugging Face Spaces](https://img.shields.io/badge/Hugging%20Face-Spaces-orange?logo=huggingface)](https://huggingface.co/spaces/new)

A simple speech emotion recognition project that predicts the emotional state of a speaker from a WAV audio file.

The app uses:
- A pre-trained TensorFlow/Keras model stored in `models/final_industry_ser_model.keras`
- Audio preprocessing and MFCC feature extraction in `src/`
- A Streamlit user interface in `app/app.py`

## What this project does

1. Loads an audio file in WAV format.
2. Trims silence and normalizes the audio.
3. Extracts MFCC features from the audio signal.
4. Runs the features through a trained model.
5. Shows the predicted emotion and confidence score in the web interface.

## Project structure

- `app/` — Streamlit interface and file uploader
- `models/` — Pre-trained TensorFlow/Keras model file
- `src/` — Python modules for preprocessing, feature extraction, and prediction
- `dataset/` — optional audio dataset for testing or experimentation
- `outputs/` — generated graphs, reports, or other output files
- `requirements.txt` — project dependencies
- `main.py` — experimental pipeline script for batch processing audio files

## Supported emotions

The model predicts one of these emotions:
- `angry`
- `fearful`
- `happy`
- `neutral`
- `sad`

## Requirements

This project is tested with:
- Python 3.10+ or 3.11
- `tensorflow==2.16.2`
- `streamlit==1.57.0`
- `librosa==0.11.0`
- `numpy==1.26.4`
- `pandas==3.0.3`
- `scikit-learn==1.8.0`
- `soundfile==0.13.1`

> Note: For Hugging Face Spaces and Linux deployment, use `tensorflow==2.16.2`. Mac-specific packages like `tensorflow-macos` and `tensorflow-metal` are not required for Spaces.

## Setup

1. Create and activate a virtual environment:

```bash
python3.11 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Run the app

Start the Streamlit interface:

```bash
streamlit run app/app.py
```

Then open the URL shown by Streamlit in your browser.

## Deploy to Hugging Face Spaces

This repository supports two deployment options.

### Option 1: Native Streamlit Space

1. Create a new Hugging Face Space.
2. Choose `Streamlit` as the SDK.
3. Push this repository to the Space.
4. Ensure `requirements.txt`, `app.py`, and `models/final_industry_ser_model.keras` are included.

Hugging Face should detect the root `app.py` wrapper and run the Streamlit app automatically.

### Option 2: Docker Space

1. Create a new Hugging Face Space.
2. Choose `Docker` as the SDK.
3. Push this repository to the Space.

The provided `Dockerfile` installs `ffmpeg` and runs Streamlit on port `7860`, so no further Docker configuration is required.

### Deploy-ready commands

Use this sequence to push the repository and deploy it on Hugging Face Spaces:

```bash
git add .
git commit -m "Deploy Speech Emotion Recognition to Hugging Face Spaces"
git push origin main
```

Then create a new Hugging Face Space and choose one of these options:

- `Streamlit` SDK: the root `app.py` wrapper will be detected automatically
- `Docker` SDK: the existing `Dockerfile` installs `ffmpeg` and runs the app on port `7860`

If you want to build locally first, make sure Docker Desktop is running and then use:

```bash
docker build -t ser-app .
docker run -p 7860:7860 ser-app
```

If the Docker daemon is not running, the build will fail with a socket connection error.

## How to use the app

1. Upload a `.wav` audio file using the file uploader.
2. Click the **Predict Emotion** button.
3. View the predicted emotion and confidence score.

## Notes for developers

- `src/preprocessing.py` handles audio loading, trimming, normalization, and length standardization.
- `src/feature_extraction.py` extracts MFCC features from the audio.
- `src/prediction.py` loads the model and returns the predicted emotion and confidence.
- `main.py` is an experimental script for batch processing audio files from `dataset/`.

## Future improvements

- Add support for more audio file formats (MP3, FLAC)
- Add real-time microphone recording
- Expand emotion labels beyond the current five classes
- Add model evaluation and result logging

## License

This project is available under the MIT License.
