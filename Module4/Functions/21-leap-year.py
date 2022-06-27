def is_year_leap(year, answer):

    if year < 1582:
        answer = "Not within the Gregorian calendar period"
        return (False, answer)
    elif (year % 4) == 0:
        if year % 100 == 0 and year % 400 != 0:
            answer = " a Common year"
            return (False, answer)
        else:
            answer = "a Leap year"
            return (True, answer)
    else:
        answer = "a Common year"
        return (False, answer)

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
answer = None
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr, answer)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
    print(yr, "is ", answer)
