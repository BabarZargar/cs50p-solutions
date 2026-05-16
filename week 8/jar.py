def main():
    capacity = int(input("Capacity: "))
    jar = Jar(capacity)

    added = int(input("Cookies to add: "))
    jar.deposit(added)

    eaten = int(input("Cookies eaten: "))
    jar.withdraw(eaten)

    print(jar)

class Jar:
    def __init__(self, capacity = 12):
        if capacity < 0:
            raise ValueError("Invalid input")
        self._capacity = capacity
        self._size = 0

    def deposit(self, n):
        if n < 0 or self._size + n > self._capacity:
            raise ValueError("Too many cookies")
        self._size += n



    def withdraw(self, n):
        if n < 0 or self._size - n < 0:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity
        ...

    @property
    def size(self):
        return self._size

    def __str__(self):
        return  "🍪"*self._size

if __name__ == "__main__":
    main()
