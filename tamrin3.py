from typing import Iterator,List,Optional,Callable

def get_positive(lst:List[int]) -> Iterator[int]:

    return filter(lambda a: a>=0,lst)
print(list(get_positive([15,0,89,-45])))


def calculate_average(lst:List[int], ignore_zero: Optional[bool]=False ) -> float:
    if ignore_zero:
        numbers= list(filter(lambda a: a!=0,lst))
    result=sum(numbers)/len(lst)
    return result

print(calculate_average([3,9,8], ignore_zero=True))

def add(x,y):
    return x+y

def multy(x,y):
    return x*y

def perform_opeation(num1:int,num2:int, a:Callable[[int ,int],int]) -> int:
    return a(num1,num2)

print(perform_opeation(1,2,multy))