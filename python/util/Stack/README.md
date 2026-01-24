# Stack (Pila)

Implementación de una pila (Stack) usando lista enlazada que sigue el principio LIFO (Last In, First Out).

## Descripción

Una pila es una estructura de datos lineal donde los elementos se insertan y eliminan desde el mismo extremo, llamado "tope" de la pila. El último elemento insertado es el primero en ser eliminado.

## Uso

```python
from stack import Stack

# Crear una nueva pila
pila = Stack()

# Verificar si está vacía
print(pila.is_empty())  # True

# Insertar elementos (push)
pila.push(10)
pila.push(20)
pila.push(30)

# Ver elemento superior sin extraer (peek)
print(pila.peek())      # 30

# Extraer elementos (pop)
elemento = pila.pop()   # 30
print(elemento)

# Mostrar todos los elementos
pila.display()          # Muestra: 20, 10

# Obtener tamaño
print(pila.length())    # 2
```

## Métodos disponibles

- `push(data)`: Inserta elemento en el tope
- `pop()`: Extrae y retorna elemento del tope
- `peek()`: Retorna elemento del tope sin extraer
- `is_empty()`: Verifica si la pila está vacía
- `display()`: Muestra todos los elementos
- `length()`: Retorna número de elementos

## Complejidad

- **Push**: O(1)
- **Pop**: O(1)
- **Peek**: O(1)
- **Length**: O(n)
- **Display**: O(n)

## Casos de uso

- Evaluación de expresiones matemáticas
- Navegación en navegadores web (historial)
- Llamadas a funciones (call stack)
- Algoritmos de backtracking