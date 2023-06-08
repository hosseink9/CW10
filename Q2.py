

class FibonacciIterator:

    def __init__(self, n):
        self.end = n
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.end == 0:
            raise StopIteration
        self.end -= 1
        res = self.first
        next_fibo = self.first + self.second
        self.first = self.second
        self.second = next_fibo
        return res


for i in FibonacciIterator(10):
    print(i)



