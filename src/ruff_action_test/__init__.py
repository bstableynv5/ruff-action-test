from datetime import date
from random import choice


def main() -> None:
    print("Hello from ruff-action-test!")
    print(junk())
    print(stuff())
    print(date.today())


def junk() -> str:
    s = choice(
        [
            "A",
            "B",
            "C",
            "D",
        ]
    )
    return s


def stuff() -> str:
    s = choice(["A", "B", "C", "D"])
    return s
