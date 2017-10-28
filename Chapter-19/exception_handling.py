try:
    num =  int(input("Enter a number: "))
    result = 10/num
    print("Result: ", result)

except ZeroDivisionError:
    print("Exception Handler for ZeroDivisionError")
    print("We cant divide a number by 0")