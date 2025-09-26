from environment import FakeChain
from environment.message_passing import MessageHandler
from environment.tools import ReadBlockchainTool, Tool, WriteBlockchainTool
from environment.world import World


class BlockchainWorld(World):

    def __init__(self, message_handler: MessageHandler, chain: FakeChain):
        super().__init__(message_handler)
        self.chain = chain 

    def get_tools(self) -> list[Tool]:
        return [ReadBlockchainTool(self.chain), 
        WriteBlockchainTool(self.chain)]