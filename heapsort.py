# Authors: Kevin Hoser and Alex Schendel
# CS 324
# HW4

# Heapsort

from math import floor
import sys
import random

heap_size = 0
test_array_lower = 1
test_array_upper = sys.maxsize

def generate_input(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(test_array_lower, test_array_upper))
    return arr

def sort(arr):
    global heap_size
    arr = build_min_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr = exchange(arr, 0, i)
        heap_size -= 1
        arr = min_heapify(arr, 0)
    return arr

def build_min_heap(arr):
    global heap_size
    heap_size = len(arr)
    for i in range(floor(len(arr) / 2), -1, -1):
        arr = min_heapify(arr, i)
    return arr

def min_heapify(arr, i):
    l = left(i)
    r = right(i)
    smallest = None
    if l < heap_size and arr[l] < arr[i]:
        smallest = l
    else:
        smallest = i
    if r < heap_size and arr[r] < arr[smallest]:
        smallest = r
    if smallest is not i:
        arr = exchange(arr, smallest, i)
        arr = min_heapify(arr, smallest)
    return arr

def left(n):
    return 2 * n + 1

def right(n):
    return (2 * n) + 2

def exchange(arr, i, j):
    tmp = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp
    return arr

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
            if not A[i-1] >= A[i]:
                isSorted = False

    print("First 5 elements: {}".format(arr))

    arr = []
    arr.append(A[-1])
    
    for i in range (-2, -6, -1):
        if abs(i) < len(A) + 1:
            arr.insert(0, A[i])
            if not A[i] >= A[i+1]:
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
    
