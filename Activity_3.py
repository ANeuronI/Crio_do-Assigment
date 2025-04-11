import time
from openai import OpenAI, RateLimitError, Timeout
from openai import OpenAIError

client = OpenAI(api_key="your_api_key_here")


# simulating a rate limit error 
try:
     response = client.ChatCompletion.create(
     model="gpt-3.5-turbo",
     messages=[{"role": "user", "content": "generate infinite tokens"}],
     max_tokens=1000000, # intentionally hitting the max token value
 )
     print(response['choices'][0]['message']['content'])

except OpenAIError as e:
      print(f"An OpenAI error occurred: {e}")



# to avoid rate limit error we will use retry logic using try-except with delays : 
max_retries = 5
for i in range(max_retries):
    try:
            response = client.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "genrate infinte tokens"}],
            )
            print( response['choices'][0]['message']['content'])
            
    except (RateLimitError, Timeout) as e:
            print(f"⚠️ Error: {e}. Retrying ({i+1}/{max_retries})...")
            time.sleep(2 ** i)  # Exponential backoff
            
    except OpenAIError as e:
        print(f" Failed after retries: {e}")


#  we can also use third party libary that simulate this: 
#  we are using tenacity for random wait and retry logic

from tenacity import retry, wait_random_exponential, stop_after_attempt

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def call_openai(prompt):
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
