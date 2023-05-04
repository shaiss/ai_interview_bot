import openai
from dotenv import load_dotenv
import os

load_dotenv()

# Load API key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_gpt3_response(prompt, model="gpt-3.5-turbo"):
  response = openai.ChatCompletion.create(
    model=model,
    messages=[{
      "role": "system",
      "content": "You are a helpful assistant."
    }, {
      "role": "user",
      "content": prompt
    }],
    temperature=0.8,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
  )
  return response.choices[0].message['content'].strip()
