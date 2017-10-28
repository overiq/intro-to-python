import datetime

def greet(name):
    print("Hello", name, "!")
    print("Today is", datetime.datetime.now())


def main():
    print("main() function called")
    greet("Jon")
    print("main() function finished")

main()