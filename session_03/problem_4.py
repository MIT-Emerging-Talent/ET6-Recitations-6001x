"""
Created on Fri Feb  7 08:32:12 2025

@author: somai
Problem: Save and Read Circle Measurements from a File
Explanation:
1. Module Importing:
Python allows you to break your code into multiple files called modules. This makes your code more organized and reusable.

You can import functions and variables from these modules into your current script to use them.
The statement from module_name import * imports all functions and variables from the module.
Once imported, you can use these functions and variables without needing to prefix them with the module name.
For example, if your module contains a function called area(radius), you can call area(5) directly after importing it.

2. File Handling:
File handling allows you to read from and write to files on your computer. This is useful for saving results or loading data for your programs. Python provides built-in functions for this:

open(filename, mode) → Opens a file, where the mode specifies what you want to do with it.
Common modes include:
'w' (write): Creates a new file or overwrites an existing one.
'r' (read): Opens an existing file for reading.
'a' (append): Adds content to the end of an existing file without overwriting.
Important: Always close the file after you're done using it to ensure the data is saved properly.

Instructions:
Create a Python module (circle_utils.py) with a function that calculates the area of a circle. This function should take the radius as input and return the area.
In a new script (main.py), follow these steps:
Step 1: Import the area function from circle_utils.
Step 2: Calculate the area of a circle with a radius of 5.
Step 3: Open a file called "circle_area.txt" in write mode and save the result (the computed area) in the file.
Step 4: Close the file after writing.
Step 5: Open the same file in read mode, read its content, and print each line.
Step 6: Close the file after reading.
"""
