"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

now = datetime.now()
current_month = now.month
current_year = now.year

terminal_input = sys.argv

# def current_calendar(year = current_year, month = current_month):
#     return calendar.month(year, month)



def monthly_calendar(year = current_year, month = current_month):
    print(year)
    print(month)
    if len(terminal_input) == 1:
        print(calendar.month(year, month))
    elif len(terminal_input) == 2:
        if len(sys.argv[1]) == 2 or len(sys.argv[1]) == 1:
            month = int(sys.argv[1])
            print(calendar.month(year, month))
        else:
            print('i am sorry your month entry is incorrect format.')
    elif len(terminal_input) == 3:
        if len(sys.argv[1]) == 2 or len(sys.argv[1]) == 1:
            if len(sys.argv[2]) == 4:
                month = int(sys.argv[1])
                year = int(sys.argv[2])
                print(calendar.month(year, month))
            else:
                print('im am sorry your year entry is in the incorrect format.')
    else:
        print('im sorry please enter minimum filename, and if you want month for this year. or 4 and year if you want another month from a different year')



monthly_calendar()