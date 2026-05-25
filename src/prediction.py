# =========================
# IMPORT LIBRARIES
# =========================

import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

from src.preprocessing import preprocess_audio
from src.feature_extraction import extract_features

# =========================
# LOAD MODEL
# =========================
MODEL_PATH = "models/final_industry_ser_model.keras"

model = tf.keras.models.load_model(MODEL_PATH)

# =========================
# LABEL ENCODER
# =========================

emotion_labels = [
    "angry",
    "fearful",
    "happy",
    "neutral",
    "sad"
]

label_encoder = LabelEncoder()

label_encoder.fit(emotion_labels)

# =========================
# PREDICTION FUNCTION
# =========================

def predict_emotion(audio_path):

    try:

        # Preprocess audio
        audio, sr = preprocess_audio(audio_path)

        # Extract features
        features = extract_features(audio, sr)

        # Reshape
        features = np.array(features)

        features = features[np.newaxis, :, np.newaxis, np.newaxis]

        # Prediction
        prediction = model.predict(features)

        predicted_class = np.argmax(prediction)

        emotion = label_encoder.inverse_transform(
            [predicted_class]
        )[0]

        confidence = np.max(prediction)

        return emotion, confidence

    except Exception as e:

        return f"Error: {str(e)}", 0