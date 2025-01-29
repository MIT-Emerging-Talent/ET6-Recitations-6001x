# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:39:16 2025
@author: Somaia

--- 4: Understanding Branching and Conditions in Python ---

Branching allows a program to make decisions based on conditions. Python uses if, elif, and else statements to evaluate whether specific conditions are true and execute different blocks of code accordingly:

- if statement: Executes the code block only if the condition is True.
- elif (else if): Checks another condition if the previous if condition was False.
- else statement: Executes a code block when none of the previous conditions are met.

For example, this program checks whether a number is positive, negative, or zero and prints a corresponding message.

Instructions:
1. Input a Number:
    - The program will prompt the user to enter a number using input().
    - Use float() to convert the input into a floating-point number for comparison.
2. Check Conditions:
    - Use an if statement to check if the number is greater than 0:
        If true, print "The number is positive".
    - Use an elif statement to check if the number is less than 0:
        If true, print "The number is negative".
    - Use an else statement to handle cases where the number is neither positive nor negative (i.e., it is zero):
        Print "The number is zero".
3. Run the Program:
    - Enter different numbers to see how the program handles positive, negative, and zero values.

Example Scenarios:
- Scenario 1:
    Input: 7.8
    Output: "The number is positive"
- Scenario 2:
    Input: -2.5
    Output: "The number is negative"
- Scenario 3:
    Input: 0
    Output: "The number is zero"
"""
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
