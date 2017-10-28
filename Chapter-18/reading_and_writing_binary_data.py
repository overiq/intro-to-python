f_source = open("source.jpg", "rb")
f_dest = open("dest.jpg", "wb")

char_count = 0

for line in f_source:
    char_count += len(line)
    f_dest.write(line)

print(char_count, "characters copied successfully")

f_source.close()
f_dest.close()