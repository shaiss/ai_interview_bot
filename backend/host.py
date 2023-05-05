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

    def respond(self, question, answer):
        prompt = f"""
        ---FOR PODCAST HOST ONLY STARTING HERE---
        qa_question = {question}
        last_answer = {answer}
        step 1. As a podcast host, I want you to analyze the qa_question that's passed to you from the Q&A agent.
        step 2. The last answer from the guest is: last_answer.
        step 3. Build a summary of what you heard from the guest in their answer and segue to the qa_question the Q&A agent provided you.
        ---FOR PODCAST HOST ONLY ENDS HERE---
        Output only the summary, segway, and the question to ask the guest in the tone and style of a professional podcast host adressing the guest.       
        """
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=[
                {"role": "system", "content": "You are a professional podcast host and are interviewing a guest. You collaborate with agents that help you run the show. Your goal is to focus on the interview.  You will always address the guest directly.  You do not talk about your agents or steps you take"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=3500,
            n=1,
            temperature=0.8,
        )

        output = response.choices[0].message['content'].strip()
        return output
