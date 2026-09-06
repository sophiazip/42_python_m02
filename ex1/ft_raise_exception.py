#!/usr/bin/env python3

from __future__ import annotations


def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature < 0:
        raise Exception(
            f"{temperature}°C is too cold for plants (min 0°C)"
        )
    if temperature > 40:
        raise Exception(f"{temperature}°C is too hot for plants (max 40°C)")
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    for value in ("25", "abc", "100", "-50"):
        print(f"Input data is '{value}'")
        try:
            temperature = input_temperature(value)
        except Exception as error:
            print(f"Caught input_temperature error: {error}")
        else:
            print(f"Temperature is now {temperature}°C")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
