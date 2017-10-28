from improved_circle import Circle

c1 = Circle(5.4)
c2 = Circle(10.5)

def print_circle_info(circle_obj):
    print("#########################")
    print("Radius of circle", format(circle_obj.get_radius(), "0.2f"))
    print("Perimeter of circle", format(circle_obj.get_perimeter(), "0.2f"))
    print("Area of circle", format(circle_obj.get_area(), "0.2f"))
    print("#########################", end="\n\n")


print_circle_info(c1) # passing circle object c1 to print_circle_info()
print_circle_info(c2) # passing circle object c2 to print_circle_info()