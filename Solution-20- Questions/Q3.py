# Write a program that checks if a 
# given year is a leap year.

year=int(input("Enter Your year :"))
if year%4 ==0 and year%100 !=0:
    print("Leap year")
elif year%400==0:
    print("Leap year")
else:
    print("sorry this is not leap year")