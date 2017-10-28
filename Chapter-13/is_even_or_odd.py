def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if is_even(num):
    print(num, "is even")
else:
    print(num, "is odd")