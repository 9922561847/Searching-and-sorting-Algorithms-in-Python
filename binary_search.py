"""
purpose: learning about binary search
Author : Pratiksha Mali
"""

pos = -1
def binary_search(list, n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2

        if list[mid] == n:
            globals()["pos"] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1


list = [1,2,3,4,5]

n = 4

if binary_search(list, n):
    print("found at : ", pos)
else:
    print("Not found ")

