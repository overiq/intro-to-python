def func_1():
    x = 100  # this x is only visible inside func_1()
    print("func_1(): x =", x)
    x = 200
    print("func_1(): x =", x)


def func_2():
    x = "str" # this x is only visible inside func_2()
    print("func_2(): x =", x)
    x = "complex"
    print("func_2(): x =", x)

# x is not visible in here

func_1()
func_2()