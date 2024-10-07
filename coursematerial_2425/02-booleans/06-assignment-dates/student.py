# write your code here

def is_valid_month(month):
    if 1 <= month <= 12:
        return True
    else:
        return False

def is_leap_year(year):
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
    
def has_30_days(month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return True
    else:
        return False

def has_31_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return True
    else:
        return False

def has_28_days(month, year):
    if month == 2 and is_leap_year(year) == False:
        return True
    else:
        return False
    
def has_29_days(month, year):
    if month == 2 and is_leap_year(year) == True:
        return True
    else:
        return False
    
def is_valid_date(day, month, year):
    if is_valid_month(month):
        if has_30_days(month):
            if 1 <= day <= 30:
                return True
            else:
                return False
        elif has_31_days(month):
            if 1 <= day <= 31:
                return True
            else:
                return False
        elif is_leap_year(year) and has_29_days(month, year):
            if 1 <= day <= 29:
                return True
            else:
                return False
        elif is_leap_year(year) == False and has_28_days(month, year):
            if 1 <= day <= 28:
                return True
            else:
                return False
        else:
            return False
    else:
        return False