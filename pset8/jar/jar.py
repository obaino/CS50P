# https://cs50.harvard.edu/python/2022/psets/8/jar/


class Jar:
    def __init__(self, capacity=12, size=0):
        """Initialize the Jar object"""
        self.capacity = capacity
        self.size = size

    def __str__(self):
        """return a string containing n cookies in the jar"""
        # return f"jar capacity is: {self.capacity} - jar size is: {self.size} / {self.size * '🍪'}"
        return self.size * '🍪'

    def deposit(self, n):
        """Deposit cookies in the jar"""
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError

    def withdraw(self, n):
        """Withdraw cookies from the jar"""
        if self.size - n >= 0:
            self.size -= n
        else:
            raise ValueError

    # Getter for capacity
    @property
    def capacity(self):
        # print(f"getter capacity: {self.capacity} was accessed")
        return self._capacity

    # Setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        # print(f"setter for capacity: {self.capacity} value is now: {capacity}")
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError

    # Getter for size
    @property
    def size(self):
        # print(f"getter size {self._size} was accessed")
        return self._size

    # Setter for size
    @size.setter
    def size(self, size):
        # print(f"setter for size: {self._size} value is now: {size}")
        self._size = size


def main():
    # cookies = Jar(-1)
    cookies = Jar(12)
    cookies.deposit(8)
    cookies.withdraw(4)
    cookies.withdraw(3)
    cookies.deposit(7)
    cookies.withdraw(6)
    cookies.deposit(3)
    cookies.withdraw(1)
    cookies.deposit(8)
    cookies.withdraw(3)
    print(cookies)


if __name__ == "__main__":
    main()
