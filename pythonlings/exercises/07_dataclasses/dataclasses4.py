"""
__post_init__ runs right after @dataclass's generated __init__ sets all fields.
Use it for validation, clamping, or computing derived fields.
Access and modify fields normally: self.value = max(self.minimum, self.value).

Implement __post_init__ to clamp self.value between minimum and maximum.
"""

# I AM NOT DONE

from dataclasses import dataclass


@dataclass
class BoundedInt:
    value: int
    minimum: int = 0
    maximum: int = 100

    def __post_init__(self):
        pass
