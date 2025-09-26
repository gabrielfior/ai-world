import abc
from environment.message_passing import MessageHandler


class AgentInterface(abc.ABC):
    
    @abc.abstractmethod
    def pre_run(self, world) -> None:
        pass
    
    @abc.abstractmethod
    def step(self, world) -> None:
        pass
    
    @abc.abstractmethod
    def post_run(self, world) -> None:
        pass

    def register_message_handler(self, message_handler: MessageHandler):
        self.message_handler = message_handler

