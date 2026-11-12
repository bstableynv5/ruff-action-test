from datetime import date
from random import choice
import os


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


def poop(arg:int)->str:
    """crap dfsd sdf sdf sd sd f sdf sdfsdfds sdfdsf dsf sdfsdf sdf sdf dsfsd fsdf sdf sdf dsf sdfd sf sdf.

    Args:
        arg: gjusdsd

    Returns:
        somethigng
    """
    os.cpu_count()
    return str(arg)