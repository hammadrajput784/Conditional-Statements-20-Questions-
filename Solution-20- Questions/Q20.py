# Create a program that evaluates if an inputted number is prime.
num=float(input("Enter your number :"))
if num%2==0 or num%3==0 or num%5==0:
    print("Prime number.")
else:
    print("not prime number.")