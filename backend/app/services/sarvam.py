import os

import requests

URL = "https://api.sarvam.ai/speech-to-text"


async def transcribe(audio: bytes, filename: str) -> str:
    """Sarvam Saaras v4 speech-to-text (REST, <30s audio)."""
    key = os.getenv("SARVAM_API_KEY")
    if not key:
        return "ನಮ್ಮ checkout ಕೆಲಸ ಮಾಡುತ್ತಿಲ್ಲ, ದಯವಿಟ್ಟು ಸರಿಪಡಿಸಿ"  # offline demo fallback
    r = requests.post(
        URL,
        headers={"api-subscription-key": key},
        files={"file": (filename, audio)},
        data={"model": "saaras:v4", "mode": "codemix", "language_code": "unknown"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json().get("transcript", "")
