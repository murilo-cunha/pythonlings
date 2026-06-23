"""
Child dataclasses inherit all parent fields; new fields come after inherited ones.
If the parent has a field with a default, the child cannot add fields without
defaults (Python's positional-argument ordering rule applies here too).

Add battery_kwh: float field to ElectricVehicle.
"""

# I AM NOT DONE

from dataclasses import dataclass


@dataclass
class Vehicle:
    make: str
    model: str
    year: int


@dataclass
class ElectricVehicle(Vehicle):
    pass
