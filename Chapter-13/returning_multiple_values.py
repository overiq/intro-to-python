def sort_two_num(num1, num2):
    if num1 < num2:
        return num1, num2
    else:
        return num2, num1


number1, number2 = sort_two_num(100, 15)
print("number1 is", number1)
print("number2 is", number2)