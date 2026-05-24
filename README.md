# Speech Emotion Recognition

Speech Emotion Recognition is a macOS-compatible project that predicts emotion from spoken audio using a Keras model and a Streamlit web interface.

## Project Structure

```
Speech_Emotion_Recognition/
├── app/
│   └── app.py                         # Streamlit web interface
├── models/
│   └── final_industry_ser_model.keras # Pre-trained TensorFlow/Keras model
├── src/
│   ├── preprocessing.py               # Audio preprocessing
│   ├── feature_extraction.py          # Feature extraction utilities
│   ├── prediction.py                  # Prediction pipeline
│   └── utils.py                       # Helper utilities
├── dataset/                           # Input audio dataset (optional)
├── outputs/                           # Generated output files
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
└── main.py                            # Experimental pipeline script
```

## What it does

- Loads a pre-trained speech emotion recognition model from `models/final_industry_ser_model.keras`
- Preprocesses uploaded WAV audio files
- Extracts MFCC features for prediction
- Displays predicted emotion and confidence in a Streamlit UI

## Requirements

This project is designed to run with:

- Python 3.11
- `tensorflow-macos==2.16.2`
- `tensorflow-metal==1.2.0`
- `streamlit==1.57.0`

> On Apple Silicon macOS, use Python 3.11 for TensorFlow compatibility. Avoid Python 3.14 or newer for this environment.

## Setup

1. Install Python 3.11.
   - Recommended: install via `pyenv` or use a Python 3.11 installer for macOS.

2. Create and activate a virtual environment:

```bash
python3.11 -m venv venv
source venv/bin/activate
```

3. Upgrade packaging tools and install dependencies:

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Run the app

Start the Streamlit interface:

```bash
streamlit run app/app.py
```

Then upload a WAV audio file and view the predicted emotion with confidence score.

## Notes

- The app currently accepts `.wav` audio files only.
- Prediction is handled by `src/prediction.py` using the loaded Keras model.
- `main.py` exists as an experimental pipeline entrypoint and may not reflect the Streamlit app workflow.

## Dependencies

Key packages used by the app:

- `streamlit`
- `tensorflow-macos`
- `tensorflow-metal`
- `librosa`
- `numpy`
- `pandas`
- `scikit-learn`
- `soundfile`

Additional dependencies in `requirements.txt` include PyTorch and torchvision for development or extension purposes.

## Emotion classes

The model predicts one of these emotions:

- angry
- fearful
- happy
- neutral
- sad

## Future improvements

- Add real-time microphone capture
- Support more audio formats
- Expand emotion label set
- Add evaluation and logging

## License

This project is available under the MIT License.
