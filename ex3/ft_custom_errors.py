#!/usr/bin/env python3

from __future__ import annotations


class GardenError(Exception):
    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "Unknown garden error")


class PlantError(GardenError):
    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "Unknown plant error")


class WaterError(GardenError):
    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "Unknown water error")


def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        raise_plant_error()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print("Testing catching all garden errors...")
    for raiser in (raise_plant_error, raise_water_error):
        try:
            raiser()
        except GardenError as error:
            print(f"Caught GardenError: {error}")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
