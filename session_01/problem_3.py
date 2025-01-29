# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:39:16 2025
@author: Somaia

--- 3: Exploring and Converting Between Variable Types in Python ---

So far, you’ve worked with integers, and now it’s time to explore more data types in Python, including float, str, and bool. Additionally, Python allows you to convert (or "cast") between different data types when needed.

For example:
- Converting a float to an integer: int(1.5) becomes 1.
- Converting a boolean to a string: str(True) becomes "True".
- Converting a string containing a number to a float: float("3.14") becomes 3.14.
Let’s put this into practice by working with variables and casting between types.

Instructions
1. Create a variable half as a float with the value 0.5.
2. Create a string variable intro with the value "Hello! How are you?".
3. Create a boolean variable is_good and assign it the value True.
4. Convert half to an integer and store the result in a new variable, half_int.
5. Convert is_good to a string and store it in a variable, is_good_str.
6. Combine intro and is_good_str using string concatenation, and assign the result to a new variable, message.
7. Print the values of half_int, is_good_str, and message.
"""

half = 0.5
intro = "Hello! How are you?"
is_good = True
half_int = int(0.5)
is_good_str = str(True)
message = intro + " " + is_good_str
print(half_int, is_good_str, message)
