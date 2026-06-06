character = input("Enter a character: ")

if 'A' <= character <= 'Z':
    print("The character is an uppercase alphabet.")
elif 'a' <= character <= 'z':
    print("The character is a lowercase alphabet.")
else:
    print("The character is not an alphabet.")