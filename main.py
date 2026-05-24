"""
Main script for Speech Emotion Recognition
"""
import sys
import os
from src.preprocessing import load_audio, normalize_audio
from src.feature_extraction import extract_mfcc, extract_mel_spectrogram
from src.prediction import EmotionPredictor
from src.utils import get_audio_files, create_directories

def main():
    """Main execution function"""
    
    # Create necessary directories
    create_directories(['outputs/graphs', 'outputs/reports'])
    
    print("🎤 Speech Emotion Recognition Pipeline")
    print("-" * 50)
    
    # Initialize predictor
    predictor = EmotionPredictor(model_path='models/final_industry_ser_model.h5')
    
    # Get audio files from dataset
    audio_files = get_audio_files('dataset')
    print(f"Found {len(audio_files)} audio files")
    
    # Process each audio file
    for audio_file in audio_files[:5]:  # Process first 5 files
        print(f"\nProcessing: {audio_file}")
        
        # Load and preprocess
        audio, sr = load_audio(audio_file)
        if audio is None:
            continue
        
        audio = normalize_audio(audio)
        
        # Extract features
        mfcc = extract_mfcc(audio, sr)
        mel_spec = extract_mel_spectrogram(audio, sr)
        
        print(f"  MFCC shape: {mfcc.shape}")
        print(f"  Mel-spectrogram shape: {mel_spec.shape}")
        
        # Predict emotion
        # prediction = predictor.predict(features)
        # emotion = predictor.get_emotion_label(prediction)
        # print(f"  Predicted emotion: {emotion}")

if __name__ == "__main__":
    main()
