import unittest
from array_list import ArrayList


class TestArrayListAdd(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_add_single_element(self):
        """_summary_
        """
        arr = ArrayList(5)
        pos = arr.add("test")
        self.assertEqual(pos, 0)
        self.assertEqual(arr.get_size(), 1)
        self.assertEqual(arr.get(0), "test")

    def test_add_multiple_elements(self):
        """_summary_
        """
        arr = ArrayList(3)
        pos1 = arr.add("first")
        pos2 = arr.add("second")
        pos3 = arr.add("third")

        self.assertEqual(pos1, 0)
        self.assertEqual(pos2, 1)
        self.assertEqual(pos3, 2)
        self.assertEqual(arr.get_size(), 3)

    def test_add_triggers_resize(self):
        """_summary_
        """
        arr = ArrayList(2)
        arr.add("item1")
        arr.add("item2")

        initial_capacity = arr.get_capacity()
        pos = arr.add("item3")

        self.assertEqual(pos, 2)
        self.assertEqual(arr.get_capacity(), initial_capacity * 2)
        self.assertEqual(arr.get_size(), 3)
        self.assertEqual(arr.get(2), "item3")

    def test_add_different_types(self):
        """_summary_
        """
        arr = ArrayList()
        arr.add(42)
        arr.add("string")
        arr.add([1, 2, 3])

        self.assertEqual(arr.get(0), 42)
        self.assertEqual(arr.get(1), "string")
        self.assertEqual(arr.get(2), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()

