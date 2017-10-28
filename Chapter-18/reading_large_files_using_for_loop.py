f = open("readme.md", "r")

for line in f:
    print(line, end="")

f.close()