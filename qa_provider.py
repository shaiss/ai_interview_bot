import os
from dotenv import load_dotenv
import openai


class QAProvider:

  def __init__(self, engine="gpt-3.5-turbo"):
    load_dotenv()
    self.name = "Q&A Provider"
    self.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = self.api_key
    self.context_list = []
    self.engine = engine

  def generate_questions(self, answer):
    context = ' '.join(self.context_list)
    prompt = f"Given the following answer provided by a guest, generate a list of relevant questions: {answer}. Context: {context}"
    response = openai.ChatCompletion.create(
      model=self.engine,
      messages=[{
        "role": "system",
        "content": "You are a helpful assistant."
      }, {
        "role": "user",
        "content": prompt
      }],
      max_tokens=4000,
      n=1,
      temperature=0.8,
    )

    questions = response.choices[0].message['content'].strip().split("\n")
    return questions

  def store_summary(self, question, answer):
    summary_prompt = f"Summarize the following Q&A: Q: {question} A: {answer}"
    response = openai.ChatCompletion.create(
      model=self.engine,
      messages=[{
        "role": "system",
        "content": "You are a helpful assistant."
      }, {
        "role": "user",
        "content": summary_prompt
      }],
      max_tokens=4000,
      n=1,
      temperature=0.8,
    )

    summary = response.choices[0].message['content'].strip()
    self.context_list.append(summary)
