'''
Remove Duplicates in-place from Sorted Array

Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.
'''

def remove_duplicates(arr):
    if len(arr) == 0:
        return 0

    i = 0  # pointer for unique elements

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1  # number of unique elements


# -------- MAIN PROGRAM --------

# Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter sorted elements: ").split()))

# Validation
if len(arr) != n:
    print("Error: Invalid input length")
else:
    k = remove_duplicates(arr)

    print("\nNumber of unique elements:", k)
    print("Array after removing duplicates:", arr[:k])