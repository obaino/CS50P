# https://cs50.harvard.edu/python/2022/psets/8/jar/

class Jar:
    def __init__(self, capacity=12, size=0):
        '''Initialize the Jar object'''
        self.capacity = capacity
        self.size = size

    def __str__(self):
        '''return a string containing n cookies in the jar'''
        return f"{self.size * '🍪'}, {self.capacity}"

    def deposit(self, n):
        '''Deposit cookies in the jar'''
        self.size = self.size + n
        return self.size

    def withdraw(self, n):
        '''Withdraw cookies from the jar'''
        self.size = self.size - n
        return self.size

    # Getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # Setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    # Getter for size
    @property
    def size(self):
        return self._size

    # Setter for capacity
    @size.setter
    def size(self, size):
        self._size = size

def main():
    cookies = Jar(12)
    cookies.deposit(3)
    cookies.deposit(8)
    cookies.withdraw(4)
    cookies.withdraw(3)
    cookies.deposit(7)
    print(cookies)

if __name__ == "__main__":
    main()