#!/usr/bin/env python3

from __future__ import annotations


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    for value in ("25", "abc"):
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
