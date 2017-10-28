f = open("readme.md", "r")

chunk = 10  # specify chunk size
data = ""

# keep looping until there is data in the file
while True:
    data = f.read(chunk)
    print(data, end="")

    # if end of file is reached, break out of the while loop
    if data == "":
        break


f.close()