import typing as t

class FakeChain:
    def __init__(self) -> None:
        self.storage: dict[str, t.Any] = {}

    def read_slot(self, slot_id: 'str') -> t.Any:
        return self.storage[slot_id]
    
    def write_to_slot(self, slot_id: 'str', value: t.Any) -> None:
        self.storage[slot_id] = value