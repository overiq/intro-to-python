import os
filename = input("Enter file name: ")

try:
    f = open(filename, "r")

    for line in f:
        print(line, end="")

    f.close()

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("You don't have the permission to read the file")

except FileExistsError:
    print("You don't have the permission to read the file")

except:
    print("Unexpected error while reading the file")

else:
    print("\nProgram ran without any problem")

finally:
    print("finally clause: This will always execute")