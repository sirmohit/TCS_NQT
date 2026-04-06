'''
Count Maximum Consecutive One's in the array
Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array..
'''
def max_consecutive_ones(arr):
    count = 0
    max_count = 0

    for num in arr:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count


# -------- MAIN PROGRAM --------

# Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements (0s and 1s): ").split()))

# Validation
if len(arr) != n:
    print("Error: Invalid input length")
else:
    result = max_consecutive_ones(arr)
    print("Maximum consecutive 1's:", result)