import datetime

greet() ## ERROR: trying to call greet() before its defined

def greet():
    print("Hello !")
    print("Today is", datetime.datetime.now())