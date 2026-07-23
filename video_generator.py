print("Video Generator Ready")
import os

HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

def check_token():
    if not HF_TOKEN:
        return "Hugging Face Token नहीं मिला।"
    return "Token Connected Successfully"
