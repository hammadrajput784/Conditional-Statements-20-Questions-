# Check if a string input is uppercase, lowercase, or a mix.
string=input("Enter your word :")
if string.isupper():
    print("upper case.")
elif string.islower():
    print("lowercase.")
else:
    print("mix")