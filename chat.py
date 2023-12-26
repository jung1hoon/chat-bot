
import openai
from dotenv import load_dotenv
import os 

load_dotenv()
openai.api_key = os.getenv('OPEN_API_KEY')


completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
