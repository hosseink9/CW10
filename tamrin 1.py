class Fib:
    def __init__(self,n) -> None:
        self.n=n
        self.one=0
        self.two=1

    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n ==0:
            raise StopIteration
        self.n+=-1
        a=self.one
        nxt=self.one + self.two
        self.one=self.two
        self.two=nxt
        return a

fibo=Fib(5)

print(next(fibo))#0
print(next(fibo))#1
print(next(fibo))#1
print(next(fibo))#2
print(next(fibo))#3
print(next(fibo))


