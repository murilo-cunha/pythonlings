"""
ABCs use nominal subtyping (explicit inheritance required).
Protocols use structural subtyping (any class with matching methods qualifies).
Use ABCs when you own the hierarchy; use Protocols for third-party or loosely
coupled code where you can't force inheritance.

Implement CsvRow.serialize() to return ",".join(str(v) for v in self.values).
"""

# I AM NOT DONE

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class Serializable(Protocol):
    def serialize(self) -> str: ...


class BaseModel(ABC):
    @abstractmethod
    def serialize(self) -> str: ...


class JsonRecord(BaseModel):
    def __init__(self, data: dict):
        self.data = data

    def serialize(self) -> str:
        import json
        return json.dumps(self.data)


class CsvRow:
    def __init__(self, values: list):
        self.values = values

    def serialize(self) -> str:
        return ""
