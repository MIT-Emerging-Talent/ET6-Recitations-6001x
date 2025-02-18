# 20.0/20.0 points (graded)
# Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return an empty list.)

# This function takes in a dictionary and an integer and returns a list.
# This is trick problem you should figure out how it is!
#def keysWithValue(aDict, target):
  #  result_list = []
#***********************************************************************************************************************************
'''
Created on Fri Feb 14 17:45:09 2025

@author: somai
Finding Keys with a Specific Value in a Dictionary
Explanation:
The goal of this problem is to find all keys in a given dictionary that are associated with a specific value (the target). The dictionary’s keys and values are both integers. You need to return a sorted list of keys whose values match the target.

For example, given the dictionary:
aDict = {5: 1, 3: 90, 4: 90, 12: 90, 22: 90, 21: 100}
If the target value is 90, the keys with this value are [3, 4, 12, 22]. Your function should return this list in sorted order. If no keys match the target, return an empty list.

Instructions:
1. Define the function keysWithValue(aDict, target), which takes a dictionary and an integer target as inputs.
2. Initialize an empty list result_list to store keys that match the target value.
3. Iterate through each key in the dictionary (aDict):
  - Check if the value associated with the key matches the target.
  - If it matches, append the key to result_list.
4. Sort result_list in increasing order.
5. Return result_list. If no keys match the target, it will remain an empty list.

Example Runs:

aDict = {5: 1, 3: 90, 4: 90, 12: 90, 22: 90, 21: 100}
print(keysWithValue(aDict, 90))
# Output: [3, 4, 12, 22]

print(keysWithValue(aDict, 100))
# Output: [21]

print(keysWithValue(aDict, 50))
Output: []
'''
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    Returns: a list of keys in aDict with the value target, sorted in increasing order.
    '''
    # Initialize an empty list to store matching keys
    result_list = []
    # Iterate through each key in the dictionary
    for item in aDict:
      
    # Check if the value matches the target
      if aDict[item] == target:
    # Append the key to the result list
        result_list.append(item)
    # Sort the list of keys in increasing order
    result_list.sort()
    # Return the sorted list
    return result_list
aDict = {5: 1, 3: 90, 4: 90, 12: 90, 22: 90, 21: 100}
print(keysWithValue(aDict, 90))
print(keysWithValue(aDict, 100))
print(keysWithValue(aDict, 50))  
