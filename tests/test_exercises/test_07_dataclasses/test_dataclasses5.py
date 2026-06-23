from dataclasses5 import ElectricVehicle, Vehicle


def test_all_fields():
    ev = ElectricVehicle(make="Tesla", model="Model 3", year=2023, battery_kwh=75.0)
    assert ev.make == "Tesla"
    assert ev.model == "Model 3"
    assert ev.year == 2023
    assert ev.battery_kwh == 75.0

def test_is_vehicle():
    ev = ElectricVehicle("Tesla", "Model 3", 2023, 75.0)
    assert isinstance(ev, Vehicle)
