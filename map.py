# 1. Map
 

"""
Syntax:
    map(func, iterable) function is passed by reference
Return: 
    <iterators>"""
def power_of_number (num):
    if num == 3:
        return num
    elif num % 2 == 0:
        return num ** 2
    else:
        return num ** 3
map_values  = map(
    power_of_number,
    range(1,20)
)
print(list(map_values))
