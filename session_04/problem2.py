
# 15/15 points (graded)
# Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

# def flatten(aList):
#    ''' 
#    aList: a list 
#    Returns a copy of aList, which is a flattened version of aList
#***********************************************************************************************************************************
#problem 2
"""
Created on Fri Feb 14 17:45:09 2025

@author: somai
Flattening a Nested List
Explanation:
Imagine you have a list containing elements that are not only integers and strings but also other lists. Your goal is to convert this nested list into a flat list where all elements appear in a single-level list without changing their order. This process is called flattening a list.

For example, a nested list like [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5] should be flattened into [1, 'a', 'cat', 2, 3, 'dog', 4, 5].

The key challenge is that the nesting can be deep and unpredictable—you don’t know how many layers of lists there might be. Recursion is a powerful tool to handle this. Each time you encounter a sublist, you recursively flatten it until all elements are in a single-level list.

Instructions:
1. Define the function flatten(aList) that takes a nested list as input and returns a flattened version.
2. Initialize an empty list called newList to store the flattened elements.
3. Iterate through each element in the given list (aList):
  - If the element is not a list, append it directly to newList.
  - If the element is a list, recursively call flatten on that sublist and extend newList with the result.
4. Finally, return newList as the flattened list.

Example Run:

print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))  
# Output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

print(flatten([1, [2, [3, [4, 5]]]]))  
# Output: [1, 2, 3, 4, 5]

print(flatten(['hello', ['world', ['!']]]))  
# Output: ['hello', 'world', '!']
"""
def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    # Initialize an empty list to store the flattened elements
    e_list = []
    
    for item in aList:
        # If the item is not a list, add it directly to e_list
        if not isinstance(item, list):  
            e_list.append(item)  
        # If the item is a list, recursively flatten it and extend e_list with the result
        else:
            e_list.extend(flatten(item))      
    
    # Return the flattened list
    return e_list

print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))  

print(flatten([1, [2, [3, [4, 5]]]]))  

print(flatten(['hello', ['world', ['!']]]))
