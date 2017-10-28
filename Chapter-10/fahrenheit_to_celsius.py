keep_calculating = 'y'

while keep_calculating == 'y':

    fah = int(input("Enter temperature in Fahrenheit: "))
    cel = (fah - 32) * 5/9
    print(format(fah, "0.2f"), "°F is same as", format(cel, "0.2f"), "°C")

    keep_calculating = input("\nWant to calculate more: ? Press y for Yes, n for N: ")


print("Program Ends")