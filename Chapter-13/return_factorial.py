def factorial(n):
    f = 1
    for i in range(n, 0, -1):
        f *= n
        n -= 1

    return f


print("Factorial of 4 is", factorial(4))
print("Factorial of 4 is", factorial(6))