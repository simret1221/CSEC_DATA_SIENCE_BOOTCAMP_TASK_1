"""this is to check the fibonacci terms"""

def fibonacci(n):
    secuence = []
    a,b = 0,1

    
    for _ in range (n):
        secuence.append(a)
        a,b = b,a+b #update a and b at the same time 
    return secuence



term = int(input("Enter a number:"))
print("fibonacci sequence:", fibonacci(term))