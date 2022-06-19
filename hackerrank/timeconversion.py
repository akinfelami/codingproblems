"""
Given a 12 time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""


def timeConversion(s):
    if s[8] == 'P':  # It is pm
        hour = int(s[:2])  # first two digits.
        if hour < 12:
            hour = hour + 12
        return str(hour) + s[2:8]
    else:  # it is morning.
        if int(s[:2]) != 12:
            return s[:8]
        else:
            # it equals twelve
            return '00' + s[2:8]
