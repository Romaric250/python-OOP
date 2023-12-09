def greetings():
    """this function greets the users"""
    print("Hi")
    
greetings()


def isPrime(n):
    """Check is a number is a prime number of not"""
    prime = True
    for i in range(2,n):
       if n % i == 0:
           prime = False
           break
       else:
           prime = True
           
    print(f"{n} is {prime}")
    
    
    
    

isPrime(19)
isPrime(21)
isPrime(23)
isPrime(29)
isPrime(7)
isPrime(14)

    