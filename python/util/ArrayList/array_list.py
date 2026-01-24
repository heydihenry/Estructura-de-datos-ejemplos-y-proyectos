"""
Docstring for python.util.array_list
"""


class ArrayList:
    """Dynamic array implementation with automatic resizing."""

    def __init__(self, capacity=100):
        """Initialize the array list."""
        self.size = 0
        self.capacity = capacity
        self.data = [None]*capacity

    def get_data(self):
        """Get data
        Returns:
            array: _data_
        """
        return self.data

    def get_size(self):
        """Get size

        Returns:
            int: size
        """
        return self.size

    def get_capacity(self):
        """Get capacity

        Returns:
            int: capacity
        """
        return self.capacity

    def set_data(self, new_data):
        """Set data

        Args:
            data (array): Array data
        """
        self.data = new_data

    def set_size(self, size):
        """Set size

        Args:
            size (int): Size
        """
        self.size = size

    def set_capacity(self, capacity):
        """Set capacity

        Args:
            capacity (int): Capacity
        """
        self.capacity = capacity

    def add(self, value):
        """Add a value to the array list."""
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        pos_object = self.size
        self.size += 1
        return pos_object

    def add_index(self, index, value):
        """Add a value in index

        Args:
            index (int): _description_
            value (object): _description_

        Raises:
            IndexError: _description_
        """
        if index >= self.capacity or index < 0:
            raise IndexError("Index out of bounds" + str(index))

        new_data = [None]*self.capacity
        self.size += 1

        for i in range(0, self.capacity):
            if i == index:
                new_data[i] = value
                continue

            if i > index:
                new_data[i] = self.data[i-1]
                continue
            new_data[i] = self.data[i]
        self.data = new_data

    def get(self, index):
        """Get a value to the array list"""
        if (index >= self.size or index < 0):
            raise IndexError("Index out of bounds" + str(index))
        return self.data[index]

    def get_pos(self, value):
        """Get a pos value to the array list"""
        for i in range(0, self.size):
            if self.data[i] == value:
                return i
        return -1


    def resize(self):
        """Resize the array list when capacity is reached."""
        self.capacity *= 2
        new_data = [None]*self.capacity
        for i in range(0, self.size):
            new_data[i] = self.data[i]
        self.data = new_data

arraytest = ArrayList(5)
arraytest.add(1)
arraytest.add(2)
arraytest.add(3)
data = arraytest.get_data()

print(data)

arraytest.add_index(5, 5)
data = arraytest.get_data()


print(data)
