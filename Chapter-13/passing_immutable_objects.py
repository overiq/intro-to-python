def func(para1):
    para1 += 100  # increment para1 by 100
    print("Inside function call, para1 =", para1)

arg1 = 100
print("Before function call, arg1 =", arg1)
func(arg1)
print("After function call, arg1 =", arg1)