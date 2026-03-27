def secLar(arr):
    lar = sec = float("-inf")
    for i in arr:
        if i>lar:
            sec,lar = lar,i

        elif i > sec and i != lar:
            i = sec

    return sec