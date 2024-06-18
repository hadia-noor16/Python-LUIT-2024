spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

countera=0
counterb=0
counterc=0

for spending in spendings:
    if spending<1000:
        countera+=1
        
    elif spending<=2500:
        counterb+=1
        
    elif spending>2500:
        counterc+=1
        
print('Numbers of months with low spendings: '+str(countera)+','+' normal spendings: '+str(counterb)+','+' high spendings: '+str(counterc)+'.')