for i in range(1, 5):
    print("Outer loop i = ", i, end="\n\n")
    for j in range (65, 75):
        print("\tInner loop chr(j) =", chr(j))
        if chr(j) == 'C':
            print("\tbreaking out of inner for loop ...\n")
            break

    print('-------------------------------------------------')