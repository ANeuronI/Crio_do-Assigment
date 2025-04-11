from openai import OpenAI
from openai import OpenAIError

client = OpenAI(api_key="your_api_key_here")

try:
    # Example of a simple API call to get a completion
    response = client.Completion.create(
        mpdel="gpt-4o",
        prompt="Write a paragraph about a unicorn.",
    )
    print(response.choices[0].text.strip())
except OpenAIError as e:
    print(f"An error occurred: {e}")    
    
