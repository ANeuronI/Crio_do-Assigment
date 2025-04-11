import time
from openai import OpenAI, RateLimitError, Timeout
from openai import OpenAIError

client = OpenAI(api_key="your_api_key_here")

# simulating a rate limit error
max_retries = 5
for i in range(max_retries):
    try:
            response = client.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "genrate infinte tokens"}],
                max_tokens=1000000,  # Intentionally high to trigger rate limit
            )
            print( response['choices'][0]['message']['content'])
            
    except (RateLimitError, Timeout) as e:
            print(f"⚠️ Error: {e}. Retrying ({i+1}/{max_retries})...")
            time.sleep(2 ** i)  # Exponential backoff
            
    except OpenAIError as e:
        print(f" Failed after retries: {e}")


