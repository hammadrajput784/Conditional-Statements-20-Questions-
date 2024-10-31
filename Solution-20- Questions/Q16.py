# Take the length of three sides and classify 
# the triangle (equilateral, isosceles, or scalene).


side1=float(input("Enter your 1st side of triangle :"))
side2=float(input("Enter your 2nd side of triangle :"))
side3=float(input("Enter your 3rd side of triangle :"))


if side1==side2 and side2==side3:

    print("Triangle is equilanteral.")

elif side1==side2 and side3!=side1 and side2:
    print("Triangle is isoceles.")
elif side1!=side2 and side2!=side3:
    print("Triangle is isoceles.")

else:
    print("Triangle is scalene.")