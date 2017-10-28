f = open("readme.md", "r")

print("First chunk:", f.read(4), end="\n\n")  # read the first 4 character
print("Second chunk:", f.read(10), end="\n\n")  # read the next 10 character
print("Third chunk:", f.read(), end="\n\n")  # read the remaining characters in the file

f.close()