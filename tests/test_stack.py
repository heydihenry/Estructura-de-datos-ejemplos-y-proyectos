"""Tests unitarios para Stack"""

import unittest
from data_structures import Stack
from data_structures.exceptions import EmptyStructureError


class TestStack(unittest.TestCase):
    """Tests unitarios para la clase Stack"""

    def setUp(self):
        """Configuración inicial para cada test"""
        self.stack = Stack()

    def test_is_empty_new_stack(self):
        """Prueba que una pila nueva esté vacía"""
        self.assertTrue(self.stack.is_empty())

    def test_is_empty_with_elements(self):
        """Prueba que una pila con elementos no esté vacía"""
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_push_single_element(self):
        """Prueba insertar un elemento"""
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.assertFalse(self.stack.is_empty())

    def test_push_multiple_elements(self):
        """Prueba insertar múltiples elementos"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(len(self.stack), 3)

    def test_pop_empty_stack(self):
        """Prueba extraer de pila vacía debe lanzar excepción"""
        with self.assertRaises(EmptyStructureError):
            self.stack.pop()

    def test_pop_single_element(self):
        """Prueba extraer único elemento"""
        self.stack.push(10)
        result = self.stack.pop()
        self.assertEqual(result, 10)
        self.assertTrue(self.stack.is_empty())

    def test_pop_multiple_elements(self):
        """Prueba extraer múltiples elementos en orden LIFO"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())

    def test_peek_empty_stack(self):
        """Prueba ver elemento de pila vacía debe lanzar excepción"""
        with self.assertRaises(EmptyStructureError):
            self.stack.peek()

    def test_peek_with_elements(self):
        """Prueba ver elemento superior sin extraer"""
        self.stack.push(7)
        self.stack.push(8)
        self.assertEqual(self.stack.peek(), 8)
        self.assertEqual(len(self.stack), 2)  # peek no debe modificar

    def test_length_empty_stack(self):
        """Prueba obtener longitud de pila vacía"""
        self.assertEqual(len(self.stack), 0)

    def test_length_with_elements(self):
        """Prueba obtener longitud de pila con elementos"""
        for i in range(5):
            self.stack.push(i)
        self.assertEqual(len(self.stack), 5)

    def test_lifo_behavior(self):
        """Prueba comportamiento LIFO (Last In, First Out)"""
        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            self.stack.push(elem)

        for elem in reversed(elements):
            self.assertEqual(self.stack.pop(), elem)

    def test_str_representation(self):
        """Prueba representación en string"""
        self.assertEqual(str(self.stack), "Stack: []")
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(str(self.stack), "Stack: [2, 1] <- top")


if __name__ == '__main__':
    unittest.main()