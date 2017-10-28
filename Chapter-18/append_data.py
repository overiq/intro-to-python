f = open("readme.md", "a")

print("Appending data to the end of the file ...")
f.write("Fourth Line\n")
f.write("Fifth Line\n")

print("Done!")

f.close()

## open the file again

print("\nOpening the file again to read the data ...\n")

f = open("readme.md", "r")

for line in f:
    print(line, end="")

f.close()