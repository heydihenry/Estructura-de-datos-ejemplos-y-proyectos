"""Ejemplos avanzados de uso de las estructuras de datos"""

from data_structures import LinkedList, Stack, Queue
from data_structures.exceptions import EmptyStructureError, IndexOutOfRangeError


def ejemplo_validacion_parentesis():
    """Ejemplo: Validar paréntesis balanceados usando Stack"""
    print("=== Validación de Paréntesis con Stack ===")
    
    def validar_parentesis(expresion):
        pila = Stack()
        pares = {'(': ')', '[': ']', '{': '}'}
        
        for char in expresion:
            if char in pares:  # Es un paréntesis de apertura
                pila.push(char)
            elif char in pares.values():  # Es un paréntesis de cierre
                if pila.is_empty():
                    return False
                if pares[pila.pop()] != char:
                    return False
        
        return pila.is_empty()
    
    expresiones = [
        "(())",
        "([{}])",
        "(()",
        "([)]",
        ""
    ]
    
    for expr in expresiones:
        resultado = validar_parentesis(expr)
        print(f"'{expr}' -> {'Válido' if resultado else 'Inválido'}")
    print()


def ejemplo_cola_impresion():
    """Ejemplo: Sistema de cola de impresión usando Queue"""
    print("=== Sistema de Cola de Impresión ===")
    
    class SistemaImpresion:
        def __init__(self):
            self.cola_trabajos = Queue()
        
        def agregar_trabajo(self, documento):
            self.cola_trabajos.enqueue(documento)
            print(f"Trabajo agregado: {documento}")
        
        def procesar_siguiente(self):
            try:
                trabajo = self.cola_trabajos.dequeue()
                print(f"Imprimiendo: {trabajo}")
                return trabajo
            except EmptyStructureError:
                print("No hay trabajos en cola")
                return None
        
        def ver_siguiente(self):
            try:
                return self.cola_trabajos.peek()
            except EmptyStructureError:
                return None
        
        def trabajos_pendientes(self):
            return len(self.cola_trabajos)
    
    sistema = SistemaImpresion()
    
    # Agregar trabajos
    sistema.agregar_trabajo("Documento1.pdf")
    sistema.agregar_trabajo("Imagen.jpg")
    sistema.agregar_trabajo("Reporte.docx")
    
    print(f"Trabajos pendientes: {sistema.trabajos_pendientes()}")
    print(f"Siguiente trabajo: {sistema.ver_siguiente()}")
    
    # Procesar trabajos
    while sistema.trabajos_pendientes() > 0:
        sistema.procesar_siguiente()
    
    sistema.procesar_siguiente()  # Intentar procesar cola vacía
    print()


def ejemplo_lista_tareas():
    """Ejemplo: Lista de tareas con LinkedList"""
    print("=== Lista de Tareas con LinkedList ===")
    
    class ListaTareas:
        def __init__(self):
            self.tareas = LinkedList()
        
        def agregar_tarea(self, tarea):
            self.tareas.add(tarea)
            print(f"Tarea agregada: {tarea}")
        
        def agregar_tarea_urgente(self, tarea):
            self.tareas.add_first(tarea)
            print(f"Tarea urgente agregada al inicio: {tarea}")
        
        def insertar_tarea_en_posicion(self, posicion, tarea):
            try:
                self.tareas.add_pos(posicion, tarea)
                print(f"Tarea insertada en posición {posicion}: {tarea}")
            except IndexOutOfRangeError as e:
                print(f"Error: {e}")
        
        def completar_tarea(self, tarea):
            if self.tareas.delete(tarea):
                print(f"Tarea completada: {tarea}")
            else:
                print(f"Tarea no encontrada: {tarea}")
        
        def ver_tarea(self, posicion):
            try:
                tarea = self.tareas.get(posicion)
                if tarea:
                    print(f"Tarea en posición {posicion}: {tarea}")
                else:
                    print(f"No hay tarea en posición {posicion}")
            except IndexOutOfRangeError as e:
                print(f"Error: {e}")
        
        def mostrar_todas(self):
            print(f"Lista de tareas: {self.tareas}")
        
        def total_tareas(self):
            return len(self.tareas)
    
    lista = ListaTareas()
    
    # Agregar tareas
    lista.agregar_tarea("Estudiar Python")
    lista.agregar_tarea("Hacer ejercicio")
    lista.agregar_tarea_urgente("Llamar al médico")
    lista.insertar_tarea_en_posicion(1, "Comprar comida")
    
    lista.mostrar_todas()
    print(f"Total de tareas: {lista.total_tareas()}")
    
    # Ver tareas específicas
    lista.ver_tarea(0)
    lista.ver_tarea(2)
    
    # Completar tareas
    lista.completar_tarea("Hacer ejercicio")
    lista.completar_tarea("Tarea inexistente")
    
    lista.mostrar_todas()
    print()


def ejemplo_manejo_excepciones():
    """Ejemplo: Manejo de excepciones"""
    print("=== Manejo de Excepciones ===")
    
    # Stack vacía
    pila = Stack()
    try:
        pila.pop()
    except EmptyStructureError as e:
        print(f"Error en Stack: {e}")
    
    # Queue vacía
    cola = Queue()
    try:
        cola.dequeue()
    except EmptyStructureError as e:
        print(f"Error en Queue: {e}")
    
    # LinkedList índice inválido
    lista = LinkedList()
    try:
        lista.get(-1)
    except IndexOutOfRangeError as e:
        print(f"Error en LinkedList: {e}")
    
    try:
        lista.add_pos(10, "dato")
    except IndexOutOfRangeError as e:
        print(f"Error en LinkedList: {e}")


if __name__ == "__main__":
    ejemplo_validacion_parentesis()
    ejemplo_cola_impresion()
    ejemplo_lista_tareas()
    ejemplo_manejo_excepciones()