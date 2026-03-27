def lar(arr):
    lar = float("-inf")
    if not arr:
        return None
    for i in arr:
        if i > lar:
            lar = i
    return lar