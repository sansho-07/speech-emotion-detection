# Speech Emotion Recognition

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
- Python 3.11
- `tensorflow-macos==2.16.2`
- `tensorflow-metal==1.2.0`
- `streamlit==1.57.0`
- `librosa==0.11.0`
- `numpy==1.26.4`
- `pandas==3.0.3`
- `scikit-learn==1.8.0`
- `soundfile==0.13.1`

> Note: The project is configured for macOS and Apple Silicon, but the code can work on other platforms if compatible TensorFlow builds are available.

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
