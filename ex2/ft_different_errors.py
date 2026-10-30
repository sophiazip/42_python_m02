#!/usr/bin/env python3

from __future__ import annotations


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 1 / 0
    elif operation_number == 2:
        with open("/non/existent/file", "r", encoding="utf-8"):
            pass
    elif operation_number == 3:
        _ = "garden" + 1  # type: ignore


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for operation in range(5):
        print(f"Testing operation {operation}...")
        try:
            garden_operations(operation)
        except (ValueError, TypeError) as error:
            print(f"Caught {error.__class__.__name__}: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        else:
            print("Operation completed successfully")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
