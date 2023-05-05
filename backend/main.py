import json
import random
import datetime
from backend.host import Host
from backend.mediator import Mediator
from backend.srt_logger import SRTLogger
from backend.config import ENABLED_AGENTS, AGENT_FOLDER

engine = "gpt-3.5-turbo"
logger = SRTLogger()
host = Host(engine=engine)
mediator = Mediator(engine=engine, enabled_agents=ENABLED_AGENTS, agent_folder=AGENT_FOLDER)

def run_conversation():
    start_time = datetime.datetime.now()
    print("Host: Welcome to the AI-powered interview. Please provide a topic for discussion.")
    
    while True:
        guest_input = input("Guest: ")
        if guest_input.lower() == "stop":
            break

        processed_input = mediator.process_input(guest_input)
        
        question = random.choice(processed_input)

        end_time = datetime.datetime.now()
        duration = end_time - start_time
        logger.log_entry("Guest", guest_input, start_time, end_time)
        
        start_time = datetime.datetime.now()
        host_response = host.respond(question, guest_input)
        end_time = start_time + duration
        logger.log_entry("Host", host_response, start_time, end_time)
        
        print(f"Host: {host_response}")
        start_time = end_time

run_conversation()
logger.save_transcript("transcript.srt")
