"""
Yeay.

Module attributes/global variables have to be defined where they are exported.

Attributes:
    GLOBAL_VAL: Some description
"""

from kjproject.some_module import (
    GLOBAL_VAR,
    SomeClass,
    SomeDataClass,
    public_function,
)

__all__ = [
    "GLOBAL_VAR",
    "SomeClass",
    "SomeDataClass",
    "public_function",
]
