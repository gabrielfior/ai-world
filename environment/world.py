from agents.base_agent import AgentInterface
from environment.message_passing import MessageHandler
from loguru import logger
from abc import ABC, abstractmethod


class World(ABC):
    # contains state of the world, including metrics and constraints.
    def __init__(self, message_handler: MessageHandler):
        self.metrics = {}
        self.constraints = {}
        self.agents = set()
        self.message_handler = message_handler
    
    @abstractmethod
    def get_tools(self):
        ...
        

    def register_agents(self, agents: list[AgentInterface]):
        for agent in agents:
            agent.register_message_handler(self.message_handler)
        self.agents.update(agents)

    def get_agents(self) -> list[AgentInterface]:
        return list(self.agents)
    
    def display_metrics(self):
        logger.debug(f"Metrics: {self.metrics}")

    def run(self, num_steps: int):
        logger.info(f"Running world for {num_steps} steps")
        for agent in self.agents:
            agent.pre_run(self)

        for _ in range(num_steps):
            agent.step(self)
            
        for agent in self.agents:
            agent.post_run(self)
        
        self.message_handler.display_messages_exchanged()
        self.display_metrics()
    
    def step(self):
        for agent in self.agents:
            agent.run(self)