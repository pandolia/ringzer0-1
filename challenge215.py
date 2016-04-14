binary=""
with open("LoveLetter.txt","r") as file:
    for char in file.read():
        if char == ' ':
            binary = binary + "0"
        if ord(char) == 160:
            binary = binary + "1"

print binary
