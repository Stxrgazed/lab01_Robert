filename = input("Enter the name of the file you want to open: ")

try:
    with open(filename, "r") as file:
        contents = file.read()

    contents = str(contents)

    print("The content of the file is:\n", contents)

except FileNotFoundError:
    print("File not found")