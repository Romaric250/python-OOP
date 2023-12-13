arr1 = [2,2,3,5,4]
arr2 = [4,6,7,8,8]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        total = arr1[i]*arr2[i]
        print(f"{arr1[i]} * {arr2[i]} = {total}")
        break
    
    