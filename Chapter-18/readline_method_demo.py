f = open("readme.md", "r")

# read first line
print("Ist line:", f.readline())

# read the fist two characters in the second line
print("The first two characters in the 2nd line:", f.read(2), end="\n\n")

# read the remaining characters int the second line
print("Remaining characters in the 2nd line:", f.readline())

# read the next line
print("3rd line:", f.readline())

# end of the file reached, so readline returns an empty string ""
print("After end of file :", f.readline())

f.close()