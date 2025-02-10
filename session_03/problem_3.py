"""
Created on Fri Feb  7 08:32:12 2025

@author: somai

Problem 3: Calculate the Sum of the First N Natural Numbers (Using Recursion)
Explanation:
Recursion is a technique where a function calls itself to solve a smaller version of the same problem. In this case, we can compute the sum of the first n natural numbers by adding n to the sum of the first n-1 natural numbers, until we reach 1.

Concepts Covered:

Recursion
Base cases and recursive calls
Instructions:
Write a function sum_n_recursive(n) that takes a positive integer n as input and returns the sum of the first n natural numbers.
Inside the function:
Define a base case: If n is equal to 1, return 1.
Otherwise, return n plus the result of sum_n_recursive(n - 1).
Test the function with several values of n (e.g., 5, 10, 100).
Example Run:

print(sum_n_recursive(5))  # Output: 15
print(sum_n_recursive(10))  # Output: 55

"""

    """Returns the sum of the first n natural numbers using recursion."""
    # Base case

    # Recursive call: sum of n and sum_n_recursive(n-1)

# Test cases

