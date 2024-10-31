# Check if a year input by the user is a century year.
year=int(input("Enter you birthday year :"))
if year/100==0:
    print("its century year")
else:
    print("its not century year")