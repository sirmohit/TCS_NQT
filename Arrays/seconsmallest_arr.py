def secSmall(arr:list) -> int:
    sm = ssm = float("inf")

    if len(arr)<2:
        return None
    
    for i in arr:
        if i < sm:
            ssm,sm = sm,i

        elif i < ssm and i != sm:
            ssm = i

    return ssm if ssm != float("inf") else None # check if there is no second largest ekement