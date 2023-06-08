from typing import List,Iterator,Optional, Callable

def get_positive_numbers(lst:List[int])->Iterator[int]:

    return filter(lambda i: i>=0,lst)

# print(list(get_positive_numbers([1,0,-1])))




def calculate_average(lst: List[int], ignor_zero: Optional[bool]= False) -> float:

    if ignor_zero:
        lst= list(filter(lambda i: i!=0,lst))

    avg=sum(lst)/len(lst)
    return avg

calculate_average([1,2,3], ignor_zero=True)


def add(a,b):
    return a+b

def perform_operation(num1:int, num2:int,op:Callable[[int, int], int])->int:
    return op(num1,num2)

print(perform_operation(1,2,add))
