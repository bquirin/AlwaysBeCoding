"""
Pair Sum Problem
Description: Given an array of numbers, find a pair that sums up to the given number.
"""

__author__ = "Brandon"

# [1, 3, 6, 2, 3, 4]
# 5 


def find_pairs(array, target):
    deja_vu = set()
    pairs = []
    
    for num in array:
        complement = target - num
        
        if complement in deja_vu:
            pairs.append((num, complement))
        
        deja_vu.add(num)    
    
    return pairs
            
    
            
        


def main(): 
    """ Main entry point of the app"""
    result = find_pairs([1, 1, 2, 2, 4, 4, 5], 5)
    print(result)
    


if __name__ == "__main__":
    main()