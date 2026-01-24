"""Implementación de una Cola (Queue) usando Lista Enlazada

Esta clase proporciona una estructura de datos de cola con operaciones
básicas siguiendo el principio FIFO (First In, First Out).
"""

from .exceptions import EmptyStructureError


class Node:
    """Nodo individual de la cola
    
    Attributes:
        data: Dato almacenado en el nodo
        next: Referencia al siguiente nodo
    """
    def __init__(self, data):
        """Inicializa un nuevo nodo

        Args:
            data: Dato a almacenar en el nodo
        """
        self.data = data
        self.next = None


class Queue:
    """Cola implementada con lista enlazada
    
    Attributes:
        head: Referencia al primer nodo de la cola (frente)
    """
    def __init__(self):
        """Inicializa una cola vacía"""
        self.head = None

    def enqueue(self, data):
        """Inserta un elemento al final de la cola

        Args:
            data: Dato a insertar en la cola
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def dequeue(self):
        """Extrae y retorna el primer elemento de la cola

        Returns:
            Primer elemento de la cola

        Raises:
            EmptyStructureError: Si la cola está vacía
        """
        if self.head is None:
            raise EmptyStructureError("No se puede hacer dequeue en una cola vacía")
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        """Retorna el primer elemento sin extraerlo de la cola

        Returns:
            Primer elemento de la cola

        Raises:
            EmptyStructureError: Si la cola está vacía
        """
        if self.head is None:
            raise EmptyStructureError("No se puede hacer peek en una cola vacía")
        return self.head.data

    def is_empty(self):
        """Verifica si la cola está vacía

        Returns:
            bool: True si la cola está vacía, False en caso contrario
        """
        return self.head is None

    def length(self):
        """Calcula y retorna el número de elementos en la cola

        Returns:
            int: Número total de elementos en la cola
        """
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def __len__(self):
        """Permite usar len() con la cola"""
        return self.length()

    def __str__(self):
        """Representación en string de la cola"""
        if self.is_empty():
            return "Queue: []"
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Queue: [" + ", ".join(elements) + "] <- rear"