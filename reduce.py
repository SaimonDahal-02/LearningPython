"""
Syntax:
    from functools import reduce
    reduce(
        func,
        iterables
    )
Return:
    Single valued data
"""
from functools import reduce
sum = reduce(
    lambda old_value, current_value: old_value + current_value,
    range(1,20)   
)
print("Sum of numbers:",sum)