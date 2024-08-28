"""
Computes the number of Sundays between 1/1/1901 to 12/31/2000 that land on the first day of the month.

Approach:
Brute force counting. Track the day of the week that the first day of each month lands 
on in a dict. The key here is to be organized to handle all the edge cases.
"""

DAYS_PER_MONTH = {
    1: 31,
    2: 28, 
    3: 31,
    4: 30, 
    5: 31,
    6: 30, 
    7: 31,
    8: 31, 
    9: 30,
    10: 31, 
    11: 30, 
    12: 31, 
}

def counting_sundays():
    year_month_day = {1900: {1: 1}}     # Day of week that the first day of the month lands on, {year: {month: day}}
    for year in range(1900, 2001):
        for month in range(1, 13):
            if year == 1900 and month == 1:
                continue
            days_in_prev_month = None
            if year % 4 == 0 and year % 100 != 0 and month == 3:
                days_in_prev_month = 29
            elif month == 1:
                days_in_prev_month = DAYS_PER_MONTH[12]
            else: 
                days_in_prev_month = DAYS_PER_MONTH[month - 1]
            
            prev_month_first_day = None
            if month == 1:
                prev_month_first_day = year_month_day[year - 1][12]
                year_month_day[year] = {}
            else:
                prev_month_first_day = year_month_day[year][month - 1]
            year_month_day[year][month] = (prev_month_first_day + days_in_prev_month) % 7

    result = 0
    for year, month_day in year_month_day.items():
        if year < 1901:
            continue
        result += sum(1 for d in month_day.values() if d == 0)
    return result

if __name__ == "__main__":
    print(f"Result = {counting_sundays()}")