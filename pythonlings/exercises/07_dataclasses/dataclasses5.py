# I AM NOT DONE

from dataclasses import dataclass


@dataclass
class Vehicle:
    make: str
    model: str
    year: int


@dataclass
class ElectricVehicle(Vehicle):
    # Fix: add field battery_kwh: float
    pass


# DON'T EDIT THE TESTS
ev = ElectricVehicle(make="Tesla", model="Model 3", year=2023, battery_kwh=75.0)
assert ev.make == "Tesla"
assert ev.model == "Model 3"
assert ev.year == 2023
assert ev.battery_kwh == 75.0
assert isinstance(ev, Vehicle)
