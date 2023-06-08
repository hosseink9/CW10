class Fib:
    def __init__(self) -> None:
        self.one=0
        self.two=1

    
    def __iter__(self):
        return self
    
    def __next__(self):
        a=self.one
        nxt=self.one + self.two
        self.one=self.two
        self.two=nxt
        return a

fibo=Fib()

print(next(fibo))#0
print(next(fibo))#1
print(next(fibo))#1
print(next(fibo))#2
print(next(fibo))#3

