import unittest
from python.util.ArrayList.array_list import ArrayList


class TestArrayListAddIndex(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def test_add_index_at_beginning(self):
        """_summary_
        """
        arr = ArrayList(5)
        arr.add("first")
        arr.add("second")
        arr.add_index(0, "new_first")

        self.assertEqual(arr.get_size(), 3)
        self.assertEqual(arr.get(0), "new_first")
        self.assertEqual(arr.get(1), "first")
        self.assertEqual(arr.get(2), "second")

    def test_add_index_in_middle(self):
        """_summary_
        """
        arr = ArrayList(5)
        arr.add("item1")
        arr.add("item2")
        arr.add("item3")
        arr.add_index(1, "middle")

        self.assertEqual(arr.get_size(), 4)
        self.assertEqual(arr.get(0), "item1")
        self.assertEqual(arr.get(1), "middle")
        self.assertEqual(arr.get(2), "item2")
        self.assertEqual(arr.get(3), "item3")

    def test_add_index_at_end(self):
        """_summary_
        """
        arr = ArrayList(5)
        arr.add("first")
        arr.add("second")
        arr.add_index(1, "last")

        self.assertEqual(arr.get_size(), 3)
        self.assertEqual(arr.get(2), "last")

    def test_add_index_negative_raises_error(self):
        """_summary_
        """
        arr = ArrayList(5)
        arr.add("test")

        with self.assertRaises(IndexError):
            arr.add_index(-1, "value")

    def test_add_index_out_of_bounds_raises_error(self):
        """_summary_
        """
        arr = ArrayList(5)
        arr.add("test")

        with self.assertRaises(IndexError):
            arr.add_index(2, "value")

    def test_add_index_triggers_resize(self):
        """_summary_
        """
        arr = ArrayList(2)
        arr.add("item1")
        arr.add("item2")

        initial_capacity = arr.get_capacity()
        arr.add_index(0, "new_item")

        self.assertEqual(arr.get_capacity(), initial_capacity * 2)
        self.assertEqual(arr.get_size(), 3)


if __name__ == '__main__':
    unittest.main()