def recursiv(n):
    print(n)
    
    if n == 0:
        return 1
    else:
        
        recursiv(n-1 )
        
recursiv(20)
