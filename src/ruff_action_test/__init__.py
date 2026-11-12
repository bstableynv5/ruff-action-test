from random import choice


def main() -> None:
    print("Hello from ruff-action-test!")
    print(junk())


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
