# Ask the user for a grade percentage and
#  display the corresponding letter grade (A, B, C, D, F).

marks=int(input("Enter your total number :"))
if marks>=95:
    print("A")
elif marks<=85 and marks>75:
    print("B")
elif marks<=75 and marks>65:
    print("C")
elif marks<=65 and marks>55:
    print("D")
else:
    print("F")