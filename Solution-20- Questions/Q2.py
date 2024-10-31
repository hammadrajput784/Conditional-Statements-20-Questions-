# Take a user’s age as input and display
#  whether they are a minor, adult, or senior citizen.

age=int(input("Enter Your age :"))
if age<18:
    print("Minor")
elif age>=18 and age<25:
    print("Adult")
else:
    print("Senior Citizen")
