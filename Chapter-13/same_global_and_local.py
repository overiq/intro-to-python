num = "global"  # global num variable

def func():
    num = "local"   # local num variable, entirely different from global num variable
    print(num)

func()
print(num)