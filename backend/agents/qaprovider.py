import os
from dotenv import load_dotenv
import openai
from backend.utils import generate_gpt3_response

class qaprovider:

  def __init__(self, engine="gpt-3.5-turbo"):
    load_dotenv()
    self.name = "Q&A Provider"
    self.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = self.api_key
    self.context_list = []
    self.engine = engine
  
  def process(self, answer):
      # Call the generate_questions method and pass the user input (answer)
      questions = self.generate_questions(answer)
      return questions
      
  def generate_questions(self, answer):
    context = ' '.join(self.context_list)
    prompt = f"Given the following answer  and context provided by a guest, generate a list of relevant questions: {answer}. Context: {context}"
    response = openai.ChatCompletion.create(
      model=self.engine,
      messages=[{
        "role": "system",
        "content": "You are a helpful assistant to a podcast host.  Your main job is to reaerch data you are given and return thoughtfull and thoughtprovking questions to the host."
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
