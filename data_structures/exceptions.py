"""Excepciones personalizadas para las estructuras de datos."""


class DataStructureError(Exception):
    """Excepción base para errores en estructuras de datos."""
    pass


class EmptyStructureError(DataStructureError):
    """Excepción lanzada cuando se intenta operar en una estructura vacía."""
    pass


class IndexOutOfRangeError(DataStructureError):
    """Excepción lanzada cuando se accede a un índice fuera de rango."""
    pass