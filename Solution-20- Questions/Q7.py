# Write a program to find 
# the largest of three numbers.
num1=int(input("Enter your 1st Nmber :"))
num2=int(input("Enter your 2st Nmber :"))
num3=int(input("Enter your 3st Nmber :"))
if num1>num2 and num1>num3:

    print("1st Number is largest")
elif num2>num3 and num2>num1:
    print("2nd Number is largest")
else:
    print("3rd Number is largest")