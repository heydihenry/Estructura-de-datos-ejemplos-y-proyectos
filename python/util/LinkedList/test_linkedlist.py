"""_summary_
"""
import unittest
from linkedlist import LinkedList
class TestLinkedList(unittest.TestCase):
    """Tests unitarios para la clase LinkedList"""

    def setUp(self):
        """Configuración inicial para cada test"""
        self.lista = LinkedList()

    def test_add_first_empty_list(self):
        """Prueba insertar elemento al inicio en lista vacía"""
        self.lista.add_first(5)
        self.assertEqual(self.lista.get(0), 5)
        self.assertEqual(self.lista.length(), 1)

    def test_add_first_multiple_elements(self):
        """Prueba insertar múltiples elementos al inicio"""
        self.lista.add_first(1)
        self.lista.add_first(2)
        self.lista.add_first(3)
        self.assertEqual(self.lista.get(0), 3)
        self.assertEqual(self.lista.get(1), 2)
        self.assertEqual(self.lista.get(2), 1)

    def test_add_empty_list(self):
        """Prueba insertar elemento al final en lista vacía"""
        self.lista.add(10)
        self.assertEqual(self.lista.get(0), 10)
        self.assertEqual(self.lista.length(), 1)

    def test_add_multiple_elements(self):
        """Prueba insertar múltiples elementos al final"""
        self.lista.add(1)
        self.lista.add(2)
        self.lista.add(3)
        self.assertEqual(self.lista.get(0), 1)
        self.assertEqual(self.lista.get(2), 3)
        self.assertEqual(self.lista.length(), 3)

    def test_add_pos_at_beginning(self):
        """Prueba insertar elemento en posición 0"""
        self.lista.add(1)
        self.lista.add(2)
        self.lista.add_pos(0, 0)
        self.assertEqual(self.lista.get(0), 0)
        self.assertEqual(self.lista.get(1), 1)

    def test_add_pos_middle(self):
        """Prueba insertar elemento en posición intermedia"""
        self.lista.add(1)
        self.lista.add(3)
        self.lista.add_pos(1, 2)
        self.assertEqual(self.lista.get(1), 2)
        self.assertEqual(self.lista.length(), 3)

    def test_add_pos_negative_index(self):
        """Prueba insertar con índice negativo debe lanzar excepción"""
        with self.assertRaises(IndexError):
            self.lista.add_pos(-1, 5)

    def test_add_pos_out_of_range(self):
        """Prueba insertar en posición fuera de rango debe lanzar excepción"""
        self.lista.add(1)
        with self.assertRaises(IndexError):
            self.lista.add_pos(5, 10)

    def test_get_valid_index(self):
        """Prueba obtener elemento con índice válido"""
        self.lista.add(10)
        self.lista.add(20)
        self.assertEqual(self.lista.get(0), 10)
        self.assertEqual(self.lista.get(1), 20)

    def test_get_invalid_index(self):
        """Prueba obtener elemento con índice fuera de rango"""
        self.lista.add(1)
        self.assertIsNone(self.lista.get(5))

    def test_get_negative_index(self):
        """Prueba obtener elemento con índice negativo debe lanzar excepción"""
        with self.assertRaises(IndexError):
            self.lista.get(-1)

    def test_get_node_existing(self):
        """Prueba buscar nodo con dato existente"""
        self.lista.add(1)
        self.lista.add(2)
        node = self.lista.get_node(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 2)

    def test_get_node_non_existing(self):
        """Prueba buscar nodo con dato no existente"""
        self.lista.add(1)
        node = self.lista.get_node(5)
        self.assertIsNone(node)

    def test_delete_first_element(self):
        """Prueba eliminar primer elemento de la lista"""
        self.lista.add(1)
        self.lista.add(2)
        result = self.lista.delete(1)
        self.assertTrue(result)
        self.assertEqual(self.lista.get(0), 2)
        self.assertEqual(self.lista.length(), 1)

    def test_delete_middle_element(self):
        """Prueba eliminar elemento intermedio de la lista"""
        self.lista.add(1)
        self.lista.add(2)
        self.lista.add(3)
        result = self.lista.delete(2)
        self.assertTrue(result)
        self.assertEqual(self.lista.get(1), 3)

    def test_delete_non_existing(self):
        """Prueba eliminar elemento no existente"""
        self.lista.add(1)
        result = self.lista.delete(5)
        self.assertFalse(result)

    def test_delete_empty_list(self):
        """Prueba eliminar elemento de lista vacía"""
        result = self.lista.delete(1)
        self.assertIsNone(result)

    def test_length_empty_list(self):
        """Prueba obtener longitud de lista vacía"""
        self.assertEqual(self.lista.length(), 0)

    def test_length_with_elements(self):
        """Prueba obtener longitud de lista con elementos"""
        for i in range(5):
            self.lista.add(i)
        self.assertEqual(self.lista.length(), 5)

if __name__ == '__main__':
    unittest.main()
