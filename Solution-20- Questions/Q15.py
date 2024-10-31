# Write a program to check if 
# a number is within a specified range
num=float(input("Enter your number :"))
minrange=float(input("Enter your minimum range :"))
maxrange=float(input("Enter your max range :"))
if num>=minrange and num<=maxrange:
    print("num is within a specified range.")
else:
    print("num is not in specified range.")