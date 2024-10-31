# Write a program that takes a temperature in Celsius and checks 
# if it’s freezing, moderate, or hot.
tem=float(input("Enter your temperature :"))
if tem<=0:
    print("Freezing")
elif tem<25:
    print("Moderate")
else:
    print("Hot")
