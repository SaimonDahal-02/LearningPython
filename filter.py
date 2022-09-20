# Filter
"""
Syntax:
    filter(func, iterable)
Return:
    <filter obj>
"""
# Filter func should return boolean value
odd_num = filter(
    lambda number: number % 2 != 0,
    range(1,20)
)
print("Odd Numbers(1-20): ",list(odd_num))

# with custom function
def check_prime(num):
    half = num // 2
    for divider in range(2, half+1):
        if num % divider == 0:
            return False
    return True

prime_num = filter(
    check_prime,
    range(1,20)
)
print("Prime Numbers(1-20): ",list(prime_num))
