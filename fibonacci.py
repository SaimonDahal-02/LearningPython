def fibonacci(N):
    a, b = 1, 2
    for _ in range (N):
        yield a
        a, b = b, a + b
print(list(fibonacci(10)))