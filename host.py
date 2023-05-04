import os
from dotenv import load_dotenv
import openai

class Host:
    def __init__(self, engine="gpt-3.5-turbo"):
        load_dotenv()
        self.name = "Host"
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.engine = engine

    def respond(self, question):
        prompt = f"As a podcast host, ask the following question to the guest as it is adding your podcast style: {question}"
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=[
                {"role": "system", "content": "You are a podcast host."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            n=1,
            temperature=0.8,
        )

        answer = response.choices[0].message['content'].strip()
        return answer
