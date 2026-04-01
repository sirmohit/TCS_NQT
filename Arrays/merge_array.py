def findUnion(arr1, arr2):
    i, j = 0, 0
    union = []

    while i < len(arr1) and j < len(arr2):
        # Avoid duplicates
        if i > 0 and arr1[i] == arr1[i - 1]:
            i += 1
            continue
        if j > 0 and arr2[j] == arr2[j - 1]:
            j += 1
            continue

        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:
            union.append(arr1[i])
            i += 1
            j += 1

    # Remaining elements
    while i < len(arr1):
        if i == 0 or arr1[i] != arr1[i - 1]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):
        if j == 0 or arr2[j] != arr2[j - 1]:
            union.append(arr2[j])
        j += 1

    return union