tuple_a = ("alpha", "beta", "gamma")
print("tuple_a:", tuple_a)
print("Length of tuple_a:", len(tuple_a))  # len() function on tuple

tuple_b = tuple(range(1,20, 2)) # i.e tuple_b = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
print("\ntuple_b:", tuple_b)
print("Highest value in tuple_b:", max(tuple_b))   # max() function on tuple
print("Lowest value in tuple_b:",min(tuple_b))   # min() function on tuple
print("Sum of elements in tuple_b:",sum(tuple_b))   # sum() function on tuple

print("\nIndex operator ([]) and Slicing operator ([:]) : ")
print("tuple_a[1]:", tuple_a[1])
print("tuple_b[len(tuple_b)-1]:", tuple_b[len(tuple_b)-1])
print("tuple_a[1:]:", tuple_a[1:])

print("\nMembership operators with tuples: ")
print("'kappa' in tuple_a: ",'kappa' in tuple_a)
print("'kappa' not in tuple_b: ",'kappa' not in tuple_b)

print("\nIterating though elements using for loop")
print("tuple_a: ", end="")
for i in tuple_a:
    print(i, end=" ")

print("\ntuple_b: ", end="")
for i in tuple_b:
    print(i, end=" ")


print("\n\nComparing tuples: ")
print("tuple_a == tuple_b:", tuple_a == tuple_b)
print("tuple_a != tuple_b:", tuple_a != tuple_b)

print("\nMultiplication and addition operators on tuples: ")
print("tuple * 2:", tuple_a * 2)
print("tuple_b + (10000, 20000): ", tuple_b + (10000, 20000))