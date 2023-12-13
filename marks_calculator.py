subjects = []
coefficients = []
marks = []

while  1:

    subject = input("Enter the different subjects you take and enter done when done 😁😁: ")
    
    if subject == "done":
        break
    
    subjects.append(subject)
 
print(subjects)
   
for sub in subjects:
        coef = input(f"enter the coeff of {sub}: ")
        coefficients.append(coef)

print(coefficients)     
     
for each_sub in subjects:
    mark = input(f"enter marks for {each_sub}: ")
    marks.append(mark)
     
# for i in marks:
#     for j in coefficients:
#         total = total * 
#         print(f"this is it i *j {}")
          
       
def Cal_Average(coef,marks):
    total_coef = 0
    total_marks = 0
    mkt = 0
    mk_total = 0
    mkstore = []
    tester = 0
    
    # for test_mark in marks:
    #     for coef_test in coef:
    #         mkt = int(test_mark)*int(coef_test)
    #         mkstore.append(mkt)
    
    for m in range(len(marks)):
        for c in range(len(coef)):
            mkt = int(marks[m]) * int(coef[m])
            tester = marks[c] #note that this line is just there for testing purposes
            mkstore.append(mkt)
            break;
    
    for coe in coef:
        total_coef = total_coef + int(coe)
    
    for mark in mkstore:
        total_marks = total_marks + int(mark)
        
    average = total_marks/total_coef if total_marks > 0 and total_coef > 0 else 0
    
    mk_total = mkt/total_coef if total_coef > 0 and mkt > 0 else 0
    return average, total_coef, total_marks
    
print(marks)


final_average,total_coef, total_marks= Cal_Average(coefficients,marks)

print(f"Average is {final_average} ")
print(f'total marks when mul by each subs coef gives: {total_marks}')
print(f'sum of coeffifent: {total_coef}')

        
