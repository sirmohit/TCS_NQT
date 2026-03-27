def reverseArr(arr:list) -> list:
    start = 0
    end = len(arr) -1
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start  = start+1
        end = end-1

    return arr