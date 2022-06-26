def is_year_leap(year):

    if (year % 400) != 0 and (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [True, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
