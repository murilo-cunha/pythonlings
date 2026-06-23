# I AM NOT DONE

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class Serializable(Protocol):
    def serialize(self) -> str:
        ...


class BaseModel(ABC):
    @abstractmethod
    def serialize(self) -> str:
        ...


class JsonRecord(BaseModel):
    def __init__(self, data: dict):
        self.data = data

    def serialize(self) -> str:
        import json
        return json.dumps(self.data)  # This is correct


class CsvRow:
    # Does NOT inherit from BaseModel — uses structural (Protocol) typing
    def __init__(self, values: list):
        self.values = values

    def serialize(self) -> str:
        return ""  # Fix: return ",".join(str(v) for v in self.values)


# DON'T EDIT THE TESTS
jr = JsonRecord({"name": "Ada"})
assert jr.serialize() == '{"name": "Ada"}'

cr = CsvRow([1, 2, 3])
assert cr.serialize() == "1,2,3"

# CsvRow satisfies Serializable (Protocol) without inheriting from it
assert isinstance(cr, Serializable)

# CsvRow is NOT a subclass of BaseModel (ABC)
assert not isinstance(cr, BaseModel)
