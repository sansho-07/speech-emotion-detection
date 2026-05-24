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

model = tf.keras.models.load_model(
   "models/final_industry_ser_model.keras"
)

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

    # Preprocess audio
    audio, sr = preprocess_audio(audio_path)

    # Extract MFCC
    features = extract_features(audio, sr)

    # Reshape for CNN
    features = np.array(features)

    features = features[np.newaxis, :, np.newaxis, np.newaxis]

    # Predict
    prediction = model.predict(features)

    predicted_class = np.argmax(prediction)

    predicted_emotion = label_encoder.inverse_transform(
        [predicted_class]
    )[0]

    confidence = np.max(prediction)

    return predicted_emotion, confidence