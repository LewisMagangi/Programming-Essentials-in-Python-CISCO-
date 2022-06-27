year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif (year % 4) == 0:
    if year % 100 == 0 and year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
else:
    print("Common year")
