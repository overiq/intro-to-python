def func(para1):
    para1.append(4)
    print("Inside function call, para1 =", para1)

arg1 = [1,2,3]
print("Before function call, arg1 =", arg1)
func(arg1)
print("After function call, arg1 =", arg1)