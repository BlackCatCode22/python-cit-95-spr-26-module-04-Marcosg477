# File Reading Example
# Demonstrates reading a file line by line

filename = "sample.txt"

try:
    file = open(filename)

    for line in file:
        print(line.strip())

    file.close()

except:
    print("File could not be opened.")