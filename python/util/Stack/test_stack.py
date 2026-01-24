"""_summary_
"""
import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    """_summary_
    """
    def setUp(self):
        self.stack = Stack()

    def test_is_empty_new_stack(self):
        """_summary_
        """
        self.assertTrue(self.stack.is_empty())

    def test_is_empty_with_elements(self):
        """_summary_
        """
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_push_single_element(self):
        """_summary_
        """
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.assertFalse(self.stack.is_empty())

    def test_push_multiple_elements(self):
        """_summary_
        """
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.length(), 3)

    def test_pop_empty_stack(self):
        """_summary_
        """
        result = self.stack.pop()
        self.assertIsNone(result)

    def test_pop_single_element(self):
        """_summary_
        """
        self.stack.push(10)
        result = self.stack.pop()
        self.assertEqual(result, 10)
        self.assertTrue(self.stack.is_empty())

    def test_pop_multiple_elements(self):
        """_summary_
        """
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())

    def test_peek_empty_stack(self):
        """_summary_
        """
        self.assertIsNone(self.stack.peek())

    def test_peek_with_elements(self):
        """_summary_
        """
        self.stack.push(7)
        self.stack.push(8)
        self.assertEqual(self.stack.peek(), 8)
        self.assertEqual(self.stack.length(), 2)  # peek no debe modificar

    def test_length_empty_stack(self):
        """_summary_
        """
        self.assertEqual(self.stack.length(), 0)

    def test_length_with_elements(self):
        """_summary_
        """
        for i in range(5):
            self.stack.push(i)
        self.assertEqual(self.stack.length(), 5)

    def test_lifo_behavior(self):
        """_summary_
        """
        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            self.stack.push(elem)

        for elem in reversed(elements):
            self.assertEqual(self.stack.pop(), elem)

if __name__ == '__main__':
    unittest.main()
