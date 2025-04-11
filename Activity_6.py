# we will create an automated content genration for blog platform --->
# it will first genrate the blog text from gpt-4
# then it will get the image from unsplash 
# then it will create audio file for the text that was genrated in previous step
# then it will format all together

import openai
import requests
import os
from dotenv import load_dotenv

load_dotenv() 

openai.api_key = os.getenv("OPENAI_API_KEY")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

# Step 1: Generate blog post with OpenAI
def generate_blog(topic):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional blog writer."},
            {"role": "user", "content": f"Write a blog post on the topic: {topic}"}
        ]
    )
    return response.choices[0].message.content.strip()

# Step 2: Fetch relevant image from Unsplash
def fetch_unsplash_image(query):
    url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)
    data = response.json()
    return data['urls']['regular']  # returns direct image URL

# Step 3: Convert blog text to audio using OpenAI TTS
def convert_to_audio(blog_text, output_file="blog_audio.mp3"):
    speech_response = openai.Audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=blog_text
    )
    with open(output_file, "wb") as f:
        f.write(speech_response.content)
    return output_file

# Driver function to run the entire workflow
def full_blog_workflow(topic):
    print("Generating blog content...")
    blog = generate_blog(topic)
    print("\nGenerated Blog:\n", blog)

    print("\nFetching related image from Unsplash...")
    image_url = fetch_unsplash_image(topic)
    print("Image URL:", image_url)

    print("\nConverting blog to audio...")
    mp3_file = convert_to_audio(blog)
    print("Audio saved as:", mp3_file)

# Run the full pipeline
if __name__ == "__main__":
    full_blog_workflow("How AI is transforming education")
