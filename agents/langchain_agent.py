import uuid
from agents.base_agent import AgentInterface
from environment.message_passing import MessageHandler
from loguru import logger


class LangchainAgent(AgentInterface):
    def __init__(self, agent_id: str|None = None):
        self.message_handler: MessageHandler = None
        self.agent_id = agent_id if agent_id else str(uuid.uuid4())

    def pre_run(self, world):
        logger.debug(f"Pre-running agent {self}")
        other_agents = [agent for agent in world.get_agents() if agent != self]
        logger.debug(f"Found agent {other_agents}")
        if other_agents:
            self.message_handler.post_message(f"Hello, I am {self.agent_id} and I am ready to run.", other_agents[0].agent_id)
    
    def run(self, world):
        logger.debug(f"Running agent {self}")
        
    
    def post_run(self, world):
        logger.debug(f"Post-running agent {self}")