""""
Write a function takes a year and returns true if it is a leap year or false other wise
"""

def is_leap_year(year):
    """
    This function takes in a year (int) as input and returns True or False if the year is a leap year or not.
    True - input year is a leap year.
    False - input year is not a leap year.

    par: year (int)

    returns: True or False (bool) 
    """

    # check if year is evenly divisible by 4
    if year%4 == 0:
        # check if year is divisible by 100
        if year%100 == 0:
            # check if year is divisible by 400
            if year%400 ==0:
                outcome = True
            else:
                outcome = False
        else:
            outcome = True
    else:
        # year is not a leap year
        outcome = False
    
    return outcome


"""
Write a function that takes in a year and month and returns the number of days in the month

"""

def month_length(year, month):
    """
    This function returns the number of days in a month.

    par: 
        month (int) - Month between 1 and 12
        year (int)
    
    returns: 
        length (int) - Number of days in the month
    """
    # create a list of month dates
    month_length_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_index = month - 1
    if month == 2:# check if month is february
        # if it is
        # check if it is a leap year
        if is_leap_year(year):
            month_length = month_length_list[month_index] + 1
        else:
            month_length = month_length_list[month_index]
    else:
        month_length = month_length_list[month_index]
    return month_length