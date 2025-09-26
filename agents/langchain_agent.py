import uuid
from agents.base_agent import AgentInterface
from environment.message_passing import MessageHandler
from loguru import logger

from environment.tools import Tool


class LangchainAgent(AgentInterface):
    def __init__(self, agent_id: str|None = None, tools: list[Tool] = []):
        self.message_handler: MessageHandler = None
        self.agent_id = agent_id if agent_id else str(uuid.uuid4())
        self.tools = tools

    def pre_run(self, world):
        logger.debug(f"Pre-running agent {self}")
        other_agents = [agent for agent in world.get_agents() if agent != self]
        logger.debug(f"Found agent {other_agents}")
        if other_agents:
            self.message_handler.post_message(f"Hello, I am {self.agent_id} and I am ready to run.", other_agents[0].agent_id)
    
    def step(self, world):
        # fetch tools
        # tell agent to use any tool to achieve goal
        logger.debug(f"Running step agent {self}")
        
        
    
    def post_run(self, world):
        logger.debug(f"Post-running agent {self}")