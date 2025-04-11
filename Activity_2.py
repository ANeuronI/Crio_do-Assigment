import openai

openai.api_key = "sk-invalid-key" 

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
except openai.error.AuthenticationError as e:
    print("🔐 Invalid API key. Please check your credentials.")


# we should use valid api-keys to get response, 
# below code will show case how to load api key from environment variable
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response.choices[0].message.content)
except openai.error.AuthenticationError as e:
    print("🔐 Invalid API key. Please check your credentials.")