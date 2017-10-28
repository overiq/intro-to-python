def factorial(n):
    f = 1
    for i in range(n, 0, -1):
        f *= n
        n -= 1

    print(f)

num = input("Enter a number: ")
factorial(int(num))