
# ToDo - implement tool as per langchain tool calling schema.
from abc import ABC, abstractmethod
import typing as t
from environment import FakeChain


class Tool(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        ...


class AbstractBlockchainTool(Tool):
    def __init__(self, chain: FakeChain) -> None:
        self.chain: FakeChain = chain


class ReadBlockchainTool(AbstractBlockchainTool):
    def execute(self, slot_id: str) -> t.Any:
        return self.chain.read_slot(slot_id)

class WriteBlockchainTool(AbstractBlockchainTool):
    def execute(self, slot_id: str, value: t.Any) -> None:
        self.chain.write_to_slot(slot_id, value)