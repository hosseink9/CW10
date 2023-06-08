from typing import List, Iterator, Optional, Callable, Any


def get_positive_numbers(nums:List[int]) -> Iterator[int]:
    return filter(lambda num: num >= 0, nums)


def calculate_average(nums: List[int], ignore_zero: Optional[bool] = False) -> float:
    if ignore_zero:
        nums = filter(lambda num: num != 0, nums)
    result = sum(nums)/len(nums)
    return result


def perform_operation(num1: int, num2: int, operation:Callable[[int, int], int]) -> Any:
    return operation(num1, num2)


def add(num1: int, num2: int) -> int:
    return num1 + num2


print(perform_operation(5 , 6 , add))