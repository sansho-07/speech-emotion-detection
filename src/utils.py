"""
Utility functions
"""
import os
import json
from pathlib import Path
from typing import Dict, List, Any

def create_directories(paths: List[str]):
    """Create directories if they don't exist"""
    for path in paths:
        os.makedirs(path, exist_ok=True)

def save_results(results: Dict[str, Any], output_path: str):
    """Save results to JSON file"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=4)

def load_config(config_path: str) -> Dict:
    """Load configuration from JSON"""
    with open(config_path, 'r') as f:
        return json.load(f)

def get_audio_files(directory: str) -> List[str]:
    """Get all audio files from directory"""
    audio_extensions = {'.wav', '.mp3', '.flac', '.ogg', '.m4a'}
    audio_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if Path(file).suffix.lower() in audio_extensions:
                audio_files.append(os.path.join(root, file))
    
    return audio_files
