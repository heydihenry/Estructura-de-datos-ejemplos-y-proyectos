"""Implementación de una Lista Enlazada Simple

Esta clase proporciona una estructura de datos de lista enlazada
con operaciones básicas de inserción, búsqueda y eliminación.
"""
class Node:
    """Nodo individual de la lista enlazada
    
    Attributes:
        data: Dato almacenado en el nodo
        next: Referencia al siguiente nodo
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    """Lista enlazada simple
    
    Attributes:
        head: Referencia al primer nodo de la lista
    """

    def __init__(self):
        self.head = None

    def add_first(self, data):
        """Inserta un elemento al inicio de la lista

        Args:
            data: Dato a insertar
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add(self, data):
        """Inserta un elemento al final de la lista

        Args:
            data: Dato a insertar
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    #Insertar valor en cierta posicion
    def add_pos(self, index, data):
        """Inserta un elemento en una posición específica

        Args:
            index (int): Posición donde insertar (0-based)
            data: Dato a insertar
            
        Raises:
            IndexError: Si el índice está fuera de rango
        """
        if index < 0:
            raise IndexError("Índice fuera de rango")

        if index == 0:
            self.add_first(data)
            return

        current = self.head
        for _ in range(index-1):
            if current is None:
                raise IndexError("Índice fuera de rango")
            current = current.next

        if current is None:
            raise IndexError("Índice fuera de rango")

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def get(self, index):
        """Obtiene el dato en una posición específica

        Args:
            index (int): Posición del elemento (0-based)

        Returns:
            Dato en la posición especificada o None si no existe

        Raises:
            IndexError: Si el índice está fuera de rango
        """
        if index < 0:
            raise IndexError("Índice fuera de rango")
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current.data

    def get_node(self, data):
        """Busca el primer nodo que contiene un dato específico

        Args:
            data: Dato a buscar

        Returns:
            Node: Nodo que contiene el dato o None si no se encuentra
        """
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None


    def delete(self, data):
        """Elimina la primera ocurrencia de un dato específico

        Args:
            data: Dato a eliminar
            
        Returns:
            bool: True si se eliminó el elemento, False si no se encontró
        """
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False


    def length(self):
        """Tamaño de la lista
            
        Returns:
            int: Tamaño total de la lista
        """
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length


