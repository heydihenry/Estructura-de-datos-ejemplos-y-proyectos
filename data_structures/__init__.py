"""Librería de Estructuras de Datos

Implementaciones educativas de estructuras de datos fundamentales en Python.
"""

from .linked_list import LinkedList
from .stack import Stack
from .queue import Queue
from .exceptions import DataStructureError, EmptyStructureError, IndexOutOfRangeError

__version__ = "1.0.0"
__all__ = ["LinkedList", "Stack", "Queue", "DataStructureError", "EmptyStructureError", "IndexOutOfRangeError"]