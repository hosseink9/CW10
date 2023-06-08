class Fibo:

    def __init__(self):
        self.first=0
        self.second=1

    def __iter__(self):
        return self

    def __next__(self):
        x = self.first
        next_fibo = self.first + self.second
        self.first = self.second
        self.second = next_fibo

        return x

fibo = Fibo()

print(next(fibo)) # Output: 0
print(next(fibo)) # Output: 1
print(next(fibo)) # Output: 1
print(next(fibo)) # Output: 2
print(next(fibo)) # Output: 3