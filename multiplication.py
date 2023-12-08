array = [1,2,3,4,5,6,7,9,10]
i = 0
while i in range(len(array)):
    
    counter = 0
   
    print(f"multiplication table of {array[i]}")
    
        
    for counter in range(1,11):
      
        answer = array[i]*counter
        
        final_answer = answer if answer % 2 == 0 else 0
      
        
      
      
        print(f"{array[i]} * {counter} = {final_answer}")
       
    
    
    i = i+1
    