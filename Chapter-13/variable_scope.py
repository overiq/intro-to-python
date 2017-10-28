global_var = 200  # a global variable

def func():

    # local_var is a local variable
    # and is only available inside func()
    local_var = 100

    print("Inside func() - local_var =", local_var)

    # accessing a global variable inside a function
    print("Inside func() - global_var =", global_var)


func()

print("Outside func() - global_var =", global_var)

# print("Outside func() - local_var =", local_var)  # ERROR: local_var is not available here