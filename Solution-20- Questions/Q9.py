# Take three sides of a triangle as input a
# nd check if they form a valid triangle.
side1=int(input("Enter 1st side of triangle :"))
side2=int(input("Enter 2nd side of triangle :"))
side3=int(input("Enter 3rd side of triangle :"))
if side1==side2 and side2==side3 and side3==side1:
    print("valid triangle.")
else:
    print("Not valid triangle.")