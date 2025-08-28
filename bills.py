n = int(input("Enter Electricity Consumption (in Units): "))

def billcalculation(x):
     if x<=100:
        cost = 100*3
     elif x<=200:
        cost = (100*3) + (x-100)*5
     else:
        cost = (100*3) + (100*5) + (x-200)*8

     if x>300:
        cost = cost*1.10

     cost += 50
     return cost
    
print(billcalculation(n))

#if i>100 and i<=200: