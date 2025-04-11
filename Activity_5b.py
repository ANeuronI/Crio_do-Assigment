from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
Open_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=Open_api_key)

response = client.images.generate(
    model="dall-e-3",
    prompt="A futuristic cityscape at night with flying cars and glowing neon lights",
    size="1024x1024",
    quality="hd",
    n=1
)

image_url = response.data[0].url
print("Generated Image URL:", image_url)
