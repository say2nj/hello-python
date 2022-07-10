
def check_leap_year(year):
    """Takes year as input, returning whether year is Leap Year or not."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month != 2:
        if month in (1,3,5,7,8,10,12):
            return 31
        elif month in (4,6,9,11):
            return 30
        else:
            return "Invalid Input"
    elif month == 2:
        if check_leap_year(year):
            return 29
        else:
            return 28

print(days_in_month(year=2022, month=13))