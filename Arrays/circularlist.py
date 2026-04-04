'''
What the program will do
Take input:
Number of elements n
Elements of the circular list
Step value k
Simulate the circular elimination
Print:
Each removed element (optional for understanding)
Final remaining element
'''

def josephus(arr, k):
    index = 0

    print("\nElimination Process:")
    
    while len(arr) > 1:
        index = (index + k - 1) % len(arr)
        removed = arr.pop(index)
        print(f"Removed: {removed}, Remaining: {arr}")

    return arr[0]


# ----------- MAIN PROGRAM -----------

# Input: number of elements
n = int(input("Enter number of elements: "))

# Input: elements
arr = list(map(int, input("Enter elements separated by space: ").split()))

# Input: k value
k = int(input("Enter the value of k: "))

# Validation
if len(arr) != n:
    print("Error: Number of elements does not match n!")
else:
    result = josephus(arr, k)
    print("\nLast remaining element:", result)