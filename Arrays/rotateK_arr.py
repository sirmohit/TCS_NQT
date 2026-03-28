# Brute Force

def rotateK(arr:list,k:int) -> list:
    tem = []
    n = len(arr)
    k = k%n

    for i in range(k):
        tem.append(arr[i])

    for i in range(k,n):
        arr[i - k] = arr[i]

    return arr[:n-k] + tem

#---------------------------------------------------------------------------------

#Optimize Inplace

# function to reverse sub-array

def reverseSub(arr:list,i:int,j:int) -> list:
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i = i+1
        j = j-1

    return arr

# function to rotate the arrary by k place

def rotateInPlaceK(arr:list,k:int) -> list:
    n = len(arr)
    k = k%n

    arr = reverseSub(arr,0,k-1)
    arr = reverseSub(arr,k,n-1)
    arr = reverseSub(arr,0,n-1)

    return arr

#-----------------------------------------------------------------------------------------------

# Using slicing

def rotateKSlice(arr:list,k:int):
    n = len(k)
    k = k%n

    return arr[k:] + arr[:k]