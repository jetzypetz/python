#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:27:06 2023

@author: eugenio.animali
"""

def hello_world():
    return 'Hello world!'

def check_day(n):
    """
    Given an integer between 1 and 7 inclusive,
    return either string 'work!' or string 'rest!'
    depending on whether the day is a workday or not
    """
    if n < 1 or n > 7:
        return None # invalid m
    
    if n < 6:
        return 'work!'
    else:
        return 'rest!'

def name_of_month(m):
    """Given an integer m between 1 and 12 inclusive,
    indicating a month of the year, returns the name of that month.
    For example: name_of_month(1) == 'January' and name_of_month(12) == 'December'.
    If the month does not exist (that is, if m is outside the legal range),
    then this function returns None.
    """
    if m < 1 or m > 12:  # Non-existent month
        return None
    
    if m == 1:
        return 'January'
    elif m == 2:
        return 'February'
    elif m == 3:
        return 'March'
    elif m == 4:
        return 'April'
    elif m == 5:
        return 'May'
    elif m == 6:
        return 'June'
    elif m == 7:
        return 'July'
    elif m == 8:
        return 'August'
    elif m == 9:
        return 'September'
    elif m == 10:
        return 'October'
    elif m == 11:
        return 'November'
    elif m == 12:
        return 'December'
    
def str_with_suffix(n):
    """Convert the integer n to a string expressing the corresponding 
    position in an ordered sequence.
    Eg. 1 becomes '1st', 2 becomes '2nd', etc.
    """
    
    if n % 100 in [11, 12, 13]:
        return str(n) + 'th'
    elif n % 10 == 1:
        return str(n) + 'st'
    elif n % 10 == 2:
        return str(n) + 'nd'
    elif n % 10 == 3:
        return str(n) + 'rd'
    else:
        return str(n) + 'th'
    
def is_leap_year(y):
    """ Return True if y is a leap year, False otherwise. """
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False
    
def number_of_days(m, y):
    if m == 2 and is_leap_year(y):
        return 29
    else:
        if m == 2:
            return 28
        elif m in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30

def date_string(d, m, y):
    
    if not name_of_month(m):
        return 'Nonexistent date'
    
    if d > number_of_days(m, y):
        return 'Nonexistent date'
    
    return 'The ' + str_with_suffix(d) + ' of ' + name_of_month(m) + ', ' + str(y)

def time_string(n):
    days = n // 86400
    hours = (n % 86400) // 3600
    minutes = (n % 3600) // 60
    seconds = n % 60
    
    if days == 0:
        days = ''
    elif days == 1:
        days = '1 day, '
    else:
        days = str(days) + ' days, '
    
    if hours == 0:
        hours = ''
    elif hours == 1:
        hours = '1 hour, '
    else:
        hours = str(hours) + ' hours, '
    
    if minutes == 0:
        minutes = ''
    elif minutes == 1:
        minutes = '1 minute, '
    else:
        minutes = str(minutes) + ' minutes, '
    
    if seconds == 1:
        seconds = '1 second'
    else:
        seconds = str(seconds) + ' seconds'
        
    return days + hours + minutes + seconds
    