i = 'fromvalue'
j = 'tovalue'
def reveseN(arr,i , j):
    for k in range((j-i+1)//2):  # imp ((j-i)+1)//2 
        arr[i + k],arr[j + k] = arr[j + k],arr[i+k]

    return arr