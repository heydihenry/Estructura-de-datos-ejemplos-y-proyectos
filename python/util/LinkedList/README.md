# Estructura-de-datos-ejemplos-y-proyectos

## LinkedList (Lista Enlazada)

Implementación de una lista enlazada simple en Python con operaciones básicas.

### Uso

```python
from python.util.LinkedList.linkedlist import LinkedList

# Crear una nueva lista
lista = LinkedList()

# Insertar elementos
lista.add_first(10)      # Insertar al inicio
lista.add(20)            # Insertar al final
lista.add_pos(1, 15)     # Insertar en posición específica

# Obtener elementos
valor = lista.get(0)     # Obtener elemento en posición 0
nodo = lista.get_node(15) # Buscar nodo con valor específico

# Eliminar elementos
lista.delete(15)         # Eliminar primera ocurrencia del valor
```

### Métodos disponibles

- `add_first(data)`: Inserta al inicio
- `add(data)`: Inserta al final
- `add_pos(index, data)`: Inserta en posición específica
- `get(index)`: Obtiene elemento por posición
- `get_node(data)`: Busca nodo por valor
- `delete(data)`: Elimina primera ocurrencia
