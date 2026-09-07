#!/usr/bin/env python3

from __future__ import annotations


class GardenError(Exception):
    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "Unknown garden error")


class PlantError(GardenError):
    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "Unknown plant error")


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def run_watering_cycle(plant_names: list[str]) -> bool:
    print("Opening watering system")
    try:
        for plant_name in plant_names:
            water_plant(plant_name)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return False
    finally:
        print("Closing watering system")
    return True


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("Testing valid plants...")
    run_watering_cycle(["Tomato", "Lettuce", "Carrots"])
    print("Testing invalid plants...")
    if not run_watering_cycle(["Tomato", "lettuce", "Carrots"]):
        print("Cleanup always happens, even with errors!")
        return
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
