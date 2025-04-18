import openai

# simulating invalid api-key error

openai.api_key = "sk-invalid-key" # intentionally taking wrong api-key

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
except openai.error.AuthenticationError as e:
    print(f"🔐 Invalid API key. Please check your credentials.{e}") 


# we should use valid api-keys to get response, 
# below code will show case how to load api key from environment variable for secure usage
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") # it will load variable name `OPENAI_API_KEY` from .env file

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response.choices[0].message.content)
except openai.error.AuthenticationError as e:
    print("🔐 Invalid API key. Please check your credentials.")
