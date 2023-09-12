# https://cs50.harvard.edu/python/2022/psets/8/jar/


class Jar:
    def __init__(self, capacity=12, size=0):
        """Initialize the Jar object"""
        self._capacity = capacity
        self._size = size

    def __str__(self):
        """return a string containing n cookies in the jar"""
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        """Deposit cookies in the jar"""
        self._size = self._size + n
        return self._size

    def withdraw(self, n):
        """Withdraw cookies from the jar"""
        self._size = self._size - n
        return self._size

    # Getter for capacity
    @property
    def capacity(self):
        print(f"{self._capacity} was accessed")
        return self._capacity

    # Setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        print(f"setter for capacity: {self._capacity} value is now: {capacity}")
        self._capacity = capacity

    # Getter for size
    @property
    def size(self):
        print(f"getter size {self._size} was accessed")
        return self._size

    # Setter for size
    @size.setter
    def size(self, size):
        print(f"setter for size: {self._size} value is now: {size}")
        self._size = size


def main():
    cookies = Jar(12)
    cookies.deposit(3)
    cookies.deposit(8)
    cookies.withdraw(4)
    cookies.withdraw(3)
    cookies.deposit(7)
    cookies.withdraw(6)
    print(cookies)


if __name__ == "__main__":
    main()
