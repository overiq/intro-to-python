num = int(input("Enter a number: "))

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False  # number is not prime
        break  # exit from for loop

if is_prime:
    print(num, "is prime")
else:
    print(num, "is not a prime")