def factorial(n):
    if not isinstance(n, int):
        raise RuntimeError("Argument must be int")

    if n < 0:
        raise RuntimeError("Argument must be >= 0")

    f = 1
    for i in range(n):
        f *= n
        n -= 1

    return f


try:
    print("Factorial of 4 is:", factorial(4))
    print("Factorial of 12 is:", factorial("12"))

except RuntimeError as e:
    print("Error:", e)