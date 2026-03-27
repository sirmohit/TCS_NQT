# Brute force
def moveZero(arr:list) -> list:
    if not arr:
        return None
    
    nonZero = []
    for i in arr:
        if i != 0:
            nonZero.append(i)

    for i in range(len(nonZero),len(arr)):
        nonZero.append(0)

    return nonZero

#------------------------------------------------------------------

# optimize version

def moveZero(arr):
    j = 0 
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j] #internal swapping using third variable by python
            j = j + 1

    return arr