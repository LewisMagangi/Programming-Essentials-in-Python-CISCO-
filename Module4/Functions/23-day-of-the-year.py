def is_year_leap(year):
    if year < 1582:
        return False
    elif (year % 4) == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if is_year_leap(yr):
        days_in_ith_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return (days_in_ith_month[month - 1])
    elif yr != is_year_leap(yr):
        days_in_ith_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return (days_in_ith_month[month - 1])
    else:
        return None

def day_of_year(year, month, day):
    days = 0
    if is_year_leap(year):
        days_in_ith_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        while month >= 1:
            for i in range(month):
                days += days_in_ith_month [i]
            return days
    elif yr != is_year_leap(year):
        days_in_ith_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        while month >= 1:
            for i in range(month):
                days += days_in_ith_month [i]
            return days
    else:
        return None


print(day_of_year(2000, 12, 31))
