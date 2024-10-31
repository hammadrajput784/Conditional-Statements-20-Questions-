# Take two numbers and an operator (+, -, *, /)
#  as input and perform the corresponding operation.
num1=float(input("Enter your 1st number :"))
operators=input("Chose your operator ( + or - or * or / ) :")

num2=float(input("Enter your 2nd number :"))

if operators == "+" :
    result= num1+num2
    print("The result is :",result)

elif operators== "-":
    result=num1-num2
    print("The result is :",result)
elif operators == "*":
    result=num1*num2
    print("The resul is :",result)
elif operators == "/" :
    result=num1/num2
    print("The result is :",result)
else:
    print("SORRY YOUR STATEMENT IS WRONG")

