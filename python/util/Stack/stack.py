"""Implementación de una Pila (Stack) usando Lista Enlazada

Esta clase proporciona una estructura de datos de pila con operaciones
básicas siguiendo el principio LIFO (Last In, First Out).
"""
class Node:
    """Nodo individual de la pila
    
    Attributes:
        data: Dato almacenado en el nodo
        next: Referencia al siguiente nodo
    """
    def __init__(self, data = None):
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
        if self.head:
            return False
        return True

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
            Elemento superior de la pila o None si está vacía
        """
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        """Retorna el elemento superior sin extraerlo de la pila

        Returns:
            Elemento superior de la pila o None si está vacía
        """
        if self.is_empty():
            return None
        return self.head.data

    def display(self):
        """Muestra todos los elementos de la pila desde el tope hacia abajo"""
        if self.is_empty():
            print("Stack Underflow")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next

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

