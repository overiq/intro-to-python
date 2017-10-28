while True:
    value = input("\nEnter a number: ")

    if value == 'q':  # if input is 'q' exit from the while loop
        print("Exiting program (break statement executed)...")
        break

    if not value.isdigit():  # if input is not a digit move on to the next iteration
       print("Enter digits only (continue statement executed)")
       continue

    value = int(value)
    print("Cube of", value, "is", value**3)  # everything is fine, just print the cube