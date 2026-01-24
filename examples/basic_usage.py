"""Ejemplos básicos de uso de las estructuras de datos"""

from data_structures import LinkedList, Stack, Queue


def ejemplo_linked_list():
    """Ejemplo de uso de LinkedList"""
    print("=== LinkedList ===")
    lista = LinkedList()
    
    # Agregar elementos
    lista.add(1)
    lista.add(2)
    lista.add(3)
    print(f"Lista después de agregar 1, 2, 3: {lista}")
    
    # Agregar al inicio
    lista.add_first(0)
    print(f"Lista después de agregar 0 al inicio: {lista}")
    
    # Obtener elemento
    print(f"Elemento en posición 1: {lista.get(1)}")
    
    # Eliminar elemento
    lista.delete(2)
    print(f"Lista después de eliminar 2: {lista}")
    
    print(f"Longitud de la lista: {len(lista)}")
    print()


def ejemplo_stack():
    """Ejemplo de uso de Stack"""
    print("=== Stack ===")
    pila = Stack()
    
    # Agregar elementos
    pila.push(1)
    pila.push(2)
    pila.push(3)
    print(f"Pila después de push 1, 2, 3: {pila}")
    
    # Ver elemento superior
    print(f"Elemento superior (peek): {pila.peek()}")
    
    # Extraer elementos
    print(f"Pop: {pila.pop()}")
    print(f"Pop: {pila.pop()}")
    print(f"Pila después de 2 pops: {pila}")
    
    print(f"Longitud de la pila: {len(pila)}")
    print()


def ejemplo_queue():
    """Ejemplo de uso de Queue"""
    print("=== Queue ===")
    cola = Queue()
    
    # Agregar elementos
    cola.enqueue(1)
    cola.enqueue(2)
    cola.enqueue(3)
    print(f"Cola después de enqueue 1, 2, 3: {cola}")
    
    # Ver primer elemento
    print(f"Primer elemento (peek): {cola.peek()}")
    
    # Extraer elementos
    print(f"Dequeue: {cola.dequeue()}")
    print(f"Dequeue: {cola.dequeue()}")
    print(f"Cola después de 2 dequeues: {cola}")
    
    print(f"Longitud de la cola: {len(cola)}")
    print()


if __name__ == "__main__":
    ejemplo_linked_list()
    ejemplo_stack()
    ejemplo_queue()