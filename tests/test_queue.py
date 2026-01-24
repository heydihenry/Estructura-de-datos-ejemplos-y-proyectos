"""Tests unitarios para Queue"""

import unittest
from data_structures import Queue
from data_structures.exceptions import EmptyStructureError


class TestQueue(unittest.TestCase):
    """Tests unitarios para la clase Queue"""

    def setUp(self):
        """Configuración inicial para cada test"""
        self.cola = Queue()

    def test_is_empty_new_queue(self):
        """Prueba que una cola nueva esté vacía"""
        self.assertTrue(self.cola.is_empty())

    def test_is_empty_with_elements(self):
        """Prueba que una cola con elementos no esté vacía"""
        self.cola.enqueue(1)
        self.assertFalse(self.cola.is_empty())

    def test_enqueue_single_element(self):
        """Prueba insertar un elemento en cola vacía"""
        self.cola.enqueue(5)
        self.assertEqual(self.cola.peek(), 5)
        self.assertFalse(self.cola.is_empty())
        self.assertEqual(len(self.cola), 1)

    def test_enqueue_multiple_elements(self):
        """Prueba insertar múltiples elementos"""
        self.cola.enqueue(1)
        self.cola.enqueue(2)
        self.cola.enqueue(3)
        self.assertEqual(self.cola.peek(), 1)  # FIFO: primero en entrar
        self.assertEqual(len(self.cola), 3)

    def test_dequeue_empty_queue(self):
        """Prueba extraer elemento de cola vacía debe lanzar excepción"""
        with self.assertRaises(EmptyStructureError):
            self.cola.dequeue()

    def test_dequeue_single_element(self):
        """Prueba extraer único elemento"""
        self.cola.enqueue(10)
        result = self.cola.dequeue()
        self.assertEqual(result, 10)
        self.assertTrue(self.cola.is_empty())

    def test_dequeue_multiple_elements(self):
        """Prueba extraer múltiples elementos en orden FIFO"""
        self.cola.enqueue(1)
        self.cola.enqueue(2)
        self.cola.enqueue(3)
    
        self.assertEqual(self.cola.dequeue(), 1)
        self.assertEqual(self.cola.dequeue(), 2)
        self.assertEqual(self.cola.dequeue(), 3)
        self.assertTrue(self.cola.is_empty())

    def test_peek_empty_queue(self):
        """Prueba ver primer elemento de cola vacía debe lanzar excepción"""
        with self.assertRaises(EmptyStructureError):
            self.cola.peek()

    def test_peek_with_elements(self):
        """Prueba ver primer elemento sin extraer"""
        self.cola.enqueue(7)
        self.cola.enqueue(8)
        self.assertEqual(self.cola.peek(), 7)
        self.assertEqual(len(self.cola), 2)  # peek no debe modificar

    def test_length_empty_queue(self):
        """Prueba obtener longitud de cola vacía"""
        self.assertEqual(len(self.cola), 0)

    def test_length_with_elements(self):
        """Prueba obtener longitud de cola con elementos"""
        for i in range(5):
            self.cola.enqueue(i)
        self.assertEqual(len(self.cola), 5)

    def test_fifo_behavior(self):
        """Prueba comportamiento FIFO (First In, First Out)"""
        elements = [1, 2, 3, 4, 5]
    
        # Insertar elementos
        for elem in elements:
            self.cola.enqueue(elem)
        
        # Extraer en el mismo orden
        for elem in elements:
            self.assertEqual(self.cola.dequeue(), elem)

    def test_mixed_operations(self):
        """Prueba operaciones mixtas de enqueue y dequeue"""
        self.cola.enqueue(1)
        self.cola.enqueue(2)
    
        self.assertEqual(self.cola.dequeue(), 1)
        self.cola.enqueue(3)

        self.assertEqual(self.cola.dequeue(), 2)
        self.assertEqual(self.cola.dequeue(), 3)
        self.assertTrue(self.cola.is_empty())

    def test_str_representation(self):
        """Prueba representación en string"""
        self.assertEqual(str(self.cola), "Queue: []")
        self.cola.enqueue(1)
        self.cola.enqueue(2)
        self.assertEqual(str(self.cola), "Queue: [1, 2] <- rear")


if __name__ == '__main__':
    unittest.main()