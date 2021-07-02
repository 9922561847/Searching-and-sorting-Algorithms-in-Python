"""
purpose : Learning about Linear search algorithm in python with examples
Author : Pratiksha Mali
Date: 02 July 2021
"""
position = -1 #created global variable position
def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['position'] = i
            return True
        i = i + 1
    return False
list = [5,8,4,6,9,2]

n = 9
if search(list, n):
    print("found at positions : ", position)
else:
    print("Not found")