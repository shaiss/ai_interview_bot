import random
import datetime
from host import Host
from qa_provider import QAProvider
from srt_logger import SRTLogger

engine = "gpt-3.5-turbo"
logger = SRTLogger()
host = Host(engine=engine)
qa_provider = QAProvider(engine=engine)
internal_conversation = True

def run_conversation():
    start_time = datetime.datetime.now()
    print("Host: Welcome to the AI-powered interview. Please provide a topic for discussion.")
    
    while True:
        guest_input = input("Guest: ")
        if guest_input.lower() == "stop":
            break

        questions = qa_provider.generate_questions(guest_input)
        if internal_conversation:
            print(f"Q&A Provider: Generated questions: {questions}")
        
        question = random.choice(questions)
        
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        logger.log_entry("Guest", guest_input, start_time, end_time)
        
        start_time = datetime.datetime.now()
        host_response = host.respond(guest_input)
        end_time = start_time + duration
        logger.log_entry("Host", host_response, start_time, end_time)
        
        print(f"Host: {host_response}")
        start_time = end_time

run_conversation()
logger.save_transcript("transcript.srt")
