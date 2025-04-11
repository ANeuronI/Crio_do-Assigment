from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
Open_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=Open_api_key)


speech_file_path = Path(__file__).parent / "speech.mp3"

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input="Today is a wonderful day to build something people love!",
    instructions="Speak in a cheerful and positive tone.",
) as response:
    response.stream_to_file(speech_file_path)