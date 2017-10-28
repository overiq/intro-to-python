from circle import *

my_circle1 = Circle(5)
my_circle2 = Circle(10)
my_circle3 = Circle(15)

print("Address of Circle objects")
print("my_circle1:", id(my_circle1))  # print the address of Circle object referenced by variable my_circle1
print("my_circle2:", id(my_circle2))  # print the address of Circle object referenced by variable my_circle2
print("my_circle3:", id(my_circle3))  # print the address of Circle object referenced by variable my_circle3
print()

print("Address of radius attribute")
print("my_circle1:", id(my_circle1.radius)) # print the address of my_circle1's radius attribute
print("my_circle2:", id(my_circle2.radius)) # print the address of my_circle2's radius attribute
print("my_circle3:", id(my_circle3.radius), end="\n\n")  # print the address of my_circle3's radius attribute

print("Initial value of radius attribute: ")
print("my_circle1's radius:", my_circle1.radius)
print("my_circle2's radius:", my_circle2.radius)
print("my_circle3's radius:", my_circle3.radius, end="\n\n")

# changing radius attribute of circle objects
my_circle1.radius = 50
my_circle2.radius = 100
my_circle3.radius = 150

print("After changing radius attribute of circle objects", end="\n\n")

print("Final value of radius attribute: ")
print("my_circle1's radius:", my_circle1.radius)
print("my_circle2's radius:", my_circle2.radius)
print("my_circle3's radius:", my_circle3.radius)