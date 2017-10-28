try:
    num1 = int(input("Enter a num1: "))
    num2 = int(input("Enter a num2: "))

    result = num1 / num2
    print("Result: ", result)

except ZeroDivisionError:
    print("\nException Handler for ZeroDivisionError")
    print("We cant divide a number by 0")

except ValueError:
    print("\nException Handler for ValueError")
    print("Invalid input: Only integers are allowed")

except:
    print("\nSome unexpected error occurred")