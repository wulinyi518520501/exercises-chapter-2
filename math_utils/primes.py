def isprime(num):
    from math import sqrt
    
    if num == 1:
        return False
    
    if num == 2:
        return True
    
    sqrt_num = int(sqrt(num))
    for i in range (2,sqrt_num+1):
        if num % i == 0:
            return False
        
    return True