'''
Problem Understanding
You are given an array
Count frequency of each element
Find:
Element with maximum frequency
Element with minimum frequency
Return those elements
'''
def find_max_min_freq(arr):
    freq = {}

    # Step 1: Count frequency
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: Initialize
    max_freq = -1
    min_freq = float('inf')
    max_ele = None
    min_ele = None

    # Step 3: Find max and min frequency elements
    for key, value in freq.items():
        if value > max_freq:
            max_freq = value
            max_ele = key

        if value < min_freq:
            min_freq = value
            min_ele = key

    return max_ele, min_ele


# 🔽 Taking input from user
arr = list(map(int, input("Enter array elements: ").split()))

max_element, min_element = find_max_min_freq(arr)

print("Element with Maximum Frequency:", max_element)
print("Element with Minimum Frequency:", min_element)