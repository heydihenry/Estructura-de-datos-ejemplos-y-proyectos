# Python Data Structures

Implementaciones educativas de estructuras de datos fundamentales en Python, diseñadas como una librería profesional.

## Instalación

```bash
# Instalación en modo desarrollo
pip install -e .

# Instalación normal
pip install .
```

## Uso Rápido

```python
from data_structures import LinkedList, Stack, Queue

# LinkedList
lista = LinkedList()
lista.add(1)
lista.add(2)
print(lista)  # [1 -> 2]

# Stack
pila = Stack()
pila.push(1)
pila.push(2)
print(pila.pop())  # 2

# Queue
cola = Queue()
cola.enqueue(1)
cola.enqueue(2)
print(cola.dequeue())  # 1
```

## Estructuras Implementadas

### LinkedList (Lista Enlazada)
- **Principio**: Estructura lineal con nodos enlazados
- **Operaciones**: `add()`, `add_first()`, `add_pos()`, `get()`, `delete()`, `length()`
- **Complejidad**: O(1) inserción al inicio, O(n) búsqueda
- **Métodos especiales**: `len()`, `str()`

### Stack (Pila)
- **Principio**: LIFO (Last In, First Out)
- **Operaciones**: `push()`, `pop()`, `peek()`, `is_empty()`, `length()`
- **Complejidad**: O(1) para todas las operaciones principales
- **Métodos especiales**: `len()`, `str()`

### Queue (Cola)
- **Principio**: FIFO (First In, First Out)
- **Operaciones**: `enqueue()`, `dequeue()`, `peek()`, `is_empty()`, `length()`
- **Complejidad**: O(1) dequeue, O(n) enqueue
- **Métodos especiales**: `len()`, `str()`

## Características

- ✅ **Instalable con pip**
- ✅ **Imports limpios**
- ✅ **Excepciones personalizadas**
- ✅ **Tests unitarios completos**
- ✅ **Docstrings descriptivos**
- ✅ **Ejemplos de uso**
- ✅ **Métodos especiales Python**
- ✅ **Estructura de librería profesional**

## Manejo de Excepciones

```python
from data_structures import Stack
from data_structures.exceptions import EmptyStructureError

pila = Stack()
try:
    pila.pop()  # Pila vacía
except EmptyStructureError as e:
    print(f"Error: {e}")
```

## Estructura del Proyecto

```
python-data-structures/
├── pyproject.toml          # Configuración moderna
├── setup.py               # Compatibilidad pip
├── LICENSE
├── README.md
├── data_structures/       # Paquete principal
│   ├── __init__.py
│   ├── linked_list.py
│   ├── stack.py
│   ├── queue.py
│   └── exceptions.py
├── tests/                 # Tests separados
│   ├── __init__.py
│   ├── test_linked_list.py
│   ├── test_stack.py
│   └── test_queue.py
└── examples/              # Ejemplos de uso
    ├── basic_usage.py
    └── advanced_examples.py
```

## Ejecutar Tests

```bash
# Todos los tests
python -m unittest discover tests/ -p "test_*.py"

# Test específico
python -m unittest tests.test_linked_list
python -m unittest tests.test_stack
python -m unittest tests.test_queue

# Con pytest (si está instalado)
pytest tests/
```

## Ejemplos

```bash
# Ejemplos básicos
python examples/basic_usage.py

# Ejemplos avanzados
python examples/advanced_examples.py
```

## Desarrollo

```bash
# Clonar repositorio
git clone <tu-repo>
cd python-data-structures

# Instalar en modo desarrollo
pip install -e .

# Ejecutar tests
python -m unittest discover tests/
```

## Licencia

MIT License - ver archivo [LICENSE](LICENSE) para detalles.