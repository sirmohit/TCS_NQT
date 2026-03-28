# wirte the all the prime numbers till n?

n = 7

def isPrime(n):
    if n<2:
        return False
    
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return False
            break
    else:
        return True


print(isPrime(n)) 

