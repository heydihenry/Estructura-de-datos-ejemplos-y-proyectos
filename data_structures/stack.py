"""Implementación de una Pila (Stack) usando Lista Enlazada

Esta clase proporciona una estructura de datos de pila con operaciones
básicas siguiendo el principio LIFO (Last In, First Out).
"""

from .exceptions import EmptyStructureError


class Node:
    """Nodo individual de la pila
    
    Attributes:
        data: Dato almacenado en el nodo
        next: Referencia al siguiente nodo
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    """Pila implementada con lista enlazada
    
    Attributes:
        head: Referencia al nodo superior de la pila
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Verifica si la pila está vacía

        Returns:
            bool: True si la pila está vacía, False en caso contrario
        """
        return self.head is None

    def push(self, data):
        """Inserta un elemento en la parte superior de la pila

        Args:
            data: Dato a insertar en la pila
        """
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def pop(self):
        """Extrae y retorna el elemento superior de la pila

        Returns:
            Elemento superior de la pila

        Raises:
            EmptyStructureError: Si la pila está vacía
        """
        if self.is_empty():
            raise EmptyStructureError("No se puede hacer pop en una pila vacía")
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        """Retorna el elemento superior sin extraerlo de la pila

        Returns:
            Elemento superior de la pila

        Raises:
            EmptyStructureError: Si la pila está vacía
        """
        if self.is_empty():
            raise EmptyStructureError("No se puede hacer peek en una pila vacía")
        return self.head.data

    def length(self):
        """Calcula y retorna el número de elementos en la pila
        
        Returns:
            int: Número total de elementos en la pila
        """
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def __len__(self):
        """Permite usar len() con la pila"""
        return self.length()

    def __str__(self):
        """Representación en string de la pila"""
        if self.is_empty():
            return "Stack: []"
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Stack: [" + ", ".join(elements) + "] <- top"