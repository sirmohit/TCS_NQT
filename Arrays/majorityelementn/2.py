'''
Find the Majority Element that occurs more than N/2 times


20

Problem Statement: Given an integer array nums of size n, return the majority element of the array.

The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

Examples
Example 1:
Input:
 nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]  
Output:
 7  
Explanation:
 The number 7 appears 5 times in the 9-sized array, making it the most frequent element.

Example 2:
Input:
 nums = [1, 1, 1, 2, 1, 2]  
Output:
 1  
Explanation:
 The number 1 appears 4 times in the 6-sized array, making it the most frequent element.
'''

def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# Input
nums = list(map(int, input("Enter elements: ").split()))

# Output
print("Majority Element:", majorityElement(nums))