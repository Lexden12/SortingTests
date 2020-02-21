# Authors: Kevin Hoser and Alex Schendel
# CS 324
# HW4

# Heapsort

from math import floor
import random
heap_size = 0
test_array_length = 10
test_array_lower = 1
test_array_upper = 100

def heapsort(arr):
    global heap_size
    arr = build_min_heap(arr)
    for i in range(len(arr) - 1, 1, -1):
        arr = exchange(arr, 0, i)
        heap_size -= 1
        arr = min_heapify(arr, 0)
    return arr

def build_min_heap(arr):
    global heap_size
    heap_size = len(arr)
    for i in range(floor(len(arr) / 2), 0, -1):
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
    return 2 * n

def right(n):
    return (2 * n) + 1

def exchange(arr, i, j):
    tmp = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp
    return arr

if __name__ == "__main__":
    arr = []
    for i in range(test_array_length):
        arr.append(random.randint(test_array_lower, test_array_upper))
    print(arr)
    print(heapsort(arr))