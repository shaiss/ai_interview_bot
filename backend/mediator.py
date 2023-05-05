import importlib
import os


class Mediator:

  def __init__(self, engine, enabled_agents, agent_folder):
    self.engine = engine
    self.agents = self.load_agents(enabled_agents, agent_folder)

  def load_agents(self, enabled_agents, agent_folder):
    agents = []
    for agent_name in enabled_agents:
      module = importlib.import_module(f"backend.{agent_folder}.{agent_name}")
      agent_class = getattr(module, agent_name)
      agents.append(agent_class(engine=self.engine))
    return agents

  def process_input(self, input_data):
      response = []
      for agent in self.agents:
          # Call the agent's process method and store the response
          response = agent.process(input_data)
      return response

