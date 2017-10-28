import datetime

def greet():
    print("Hello !")
    print("Today is", datetime.datetime.now())

print("Before calling greet()")
greet()
print("After calling greet()")