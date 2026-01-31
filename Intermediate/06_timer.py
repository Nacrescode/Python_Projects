"""
Timer class example.

This module defines a Timer class that stores time
in hours, minutes, and seconds.

The timer can move forward or backward by one second
and can be printed in hh:mm:ss format.
"""


def two_digits(val):
    """
    Convert a number to a two-digit string.

    If the number has one digit, add a leading zero.
    Example:
    5  -> "05"
    12 -> "12"
    """
    s = str(val)          # convert number to string
    if len(s) == 1:       # check if it has one digit
        s = '0' + s       # add leading zero
    return s              # return formatted string


class Timer:
    """
    Timer class that counts time in hours, minutes, and seconds.
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Create a new Timer object.

        hours   : 0–23
        minutes : 0–59
        seconds : 0–59
        """
        self.__hours = hours       # private hour value
        self.__minutes = minutes  # private minute value
        self.__seconds = seconds  # private second value

    def __str__(self):
        """
        Return the time as a string in hh:mm:ss format.
        """
        return (
            two_digits(self.__hours) + ":" +
            two_digits(self.__minutes) + ":" +
            two_digits(self.__seconds)
        )

    def next_second(self):
        """
        Move the timer forward by one second.
        """
        self.__seconds += 1                    # increase seconds

        if self.__seconds > 59:                # second overflow
            self.__seconds = 0
            self.__minutes += 1                # increase minutes

            if self.__minutes > 59:            # minute overflow
                self.__minutes = 0
                self.__hours += 1              # increase hours

                if self.__hours > 23:          # hour overflow
                    self.__hours = 0

    def prev_second(self):
        """
        Move the timer backward by one second.
        """
        self.__seconds -= 1                    # decrease seconds

        if self.__seconds < 0:                 # second underflow
            self.__seconds = 59
            self.__minutes -= 1                # decrease minutes

            if self.__minutes < 0:             # minute underflow
                self.__minutes = 59
                self.__hours -= 1              # decrease hours

                if self.__hours < 0:           # hour underflow
                    self.__hours = 23


# --- Test code ---

timer = Timer(23, 59, 59)
print(timer)          # 23:59:59

timer.next_second()
print(timer)          # 00:00:00

timer.prev_second()
print(timer)          # 23:59:59
