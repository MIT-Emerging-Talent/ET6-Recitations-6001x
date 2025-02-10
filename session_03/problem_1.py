"""
Created on Fri Feb  7 08:32:12 2025

@author: somai
Problem 1: Searching for a Character in a Sorted String Using Bisection Search
Explanation:
Imagine you are searching for a word in a dictionary. Instead of flipping through each page one by one, you open the book near the middle, check if the word is there, and then decide whether to look in the first or second half. This is the core idea of bisection search—it helps us find things quickly by repeatedly reducing the number of possibilities.

When searching for a character in a sorted string, we don’t need to scan from left to right. Instead, we:

Start by considering the entire string.
Pick a middle character and compare it with the target letter.
If it matches, we are done!
If it’s smaller than what we need, then the target must be in the second half (since the string is sorted).
If it’s larger, then the target must be in the first half.
Ignore the half that cannot contain the target and repeat the process with the remaining part of the string.
We keep dividing the problem in half until we either find the target or determine it’s not there.
Since we eliminate half of the search space at every step, this method is much faster than checking one letter at a time.

Instructions:
Define a sorted string (e.g., "acegikm") where letters are arranged in increasing order.
Write a function find_char_bisection(sorted_str, target) to search for a target letter efficiently.
Instead of scanning every letter, start by looking at a letter near the middle of the string.
Use two markers:
One at the beginning (low)
One at the end (high)
While there’s still a meaningful range to search:
Find the middle position.
Compare this letter with the target:
If it's the correct letter, return its position.
If it comes before the target, shift focus to the latter half of the string.
If it comes after the target, shift focus to the earlier half.
Keep repeating until either:
You find the target letter.
The range becomes too small, meaning the letter isn’t in the string.
Example Run:

print(find_char_bisection("acegikm", "g"))  # Output: 3  
print(find_char_bisection("acegikm", "m"))  # Output: 6  
print(find_char_bisection("acegikm", "b"))  # Output: -1  (not found) 
"""

    #Search for a target character in a sorted string using bisection search.
    # Starting index of the search range

    # Ending index of the search range


    # Calculate the middle index
    
    # Character at the middle index

    
    # Target found, return its position
  
    # Target is in the right half, adjust low index
   
    # Target is in the left half, adjust high index

     # Target not found, return -1


# Test cases

