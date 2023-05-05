import importlib
import os

class Mediator:

    def __init__(self, engine, enabled_agents, agent_folder):
        self.engine = engine
        self.agents = self.load_agents(enabled_agents, agent_folder)

    def load_agents(self, enabled_agents, agent_folder):
        agents = []
        for agent_name in enabled_agents:
            module = importlib.import_module(f"{agent_folder}.{agent_name}")
            agent_class = getattr(module, agent_name.capitalize())
            agents.append(agent_class(engine=self.engine))
        return agents

    def process_input(self, input_text):
        data = {'input': input_text, 'questions': []}
        for agent in self.agents:
            agent.process(data)
        return data
