"""A tool for mathematical analysis of Magic the Gathering"""
from .card import BasicLand, Card

from typing import Tuple

__version__ = "0.0.1"  # type: str

colors = (
    "Blue",
    "Red",
    "Black",
    "White",
    "Green",
)  # type: Tuple[str, str, str, str, str]
