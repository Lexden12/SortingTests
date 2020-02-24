# Authors: Kevin Hoser and Alex Schendel
# CS 324
# HW4

# Radixsort

from math import floor
import sys
import random

test_array_lower = 1
test_array_upper = sys.maxsize

# returns an array with n random ints
def generate_input(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(test_array_lower, test_array_upper))
    return arr

# an implementation of radixsort
def sort(arr):
    max_int = max(arr)
    digits = len(str(max_int))

    for d in range(0, digits):
        arr = stable_sort(d, arr)
        
    return arr

# sorts an array localized on a digit d
def stable_sort(d, arr):
    buckets = [ [] for i in range(10) ]
    
    for i in range(len(arr)):
        s = str(arr[i])
        
        if len(s) < d + 1:
            buckets[0].append(arr[i])
        else:
            b = int(s[-(d+1)]) # determine the num at digit d from s
                               # eg. num = 768, 8 is d = 0, 6 is d = 1, 7 is d = 2
            buckets[b].append(arr[i])
        
    arr = []
    for i in range(len(buckets)):
        arr.extend(buckets[i])
        
    return arr       

# prints the first 5 and last 
def check_output(A):
    arr = []
    isSorted = True

    if len(A) <= 1:
        print("The array is already sorted: {}".format(A))
        return True

    arr.append(A[0])
              
    for i in range (1, 5):
        if i < len(A):
            arr.append(A[i])
            if not A[i-1] <= A[i]:
                isSorted = False

    print("First 5 elements: {}".format(arr))

    arr = []
    arr.append(A[-1])
    
    for i in range (-2, -6, -1):
        if abs(i) < len(A) + 1:
            arr.insert(0, A[i])
            if not A[i] <= A[i+1]:
                isSorted = False

    print("Last 5 elements: {}".format(arr))

    if isSorted:
        print("The array is sorted.")
    else:
        print("The array is NOT sorted.")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid amount of arguments")
        exit()
    
    n = floor(float(sys.argv[1]))
    if n < 1:
        print("n needs to be greater than 0")
        exit()
        
    arr = generate_input(n)
    check_output(arr)   
    print("\n =====SORTING THE ARRAY====== \n")
    arr = sort(arr)
    check_output(arr)
    
