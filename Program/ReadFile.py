file = open("test.txt")

# read = file.read()
# print(read)
print("=======================")
line = file.readline()

while line != "":
    print(line)
    line = file.readline()

file.close()

