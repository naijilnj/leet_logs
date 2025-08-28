n = int(input("Enter a Number: "))
L = []
L1 = []
for i in range(1,n+1):
    L.append(i)

for j in L:
        L1.append(j**2)

square_dict={}

for i in L:
    square_dict[i]=[i**2]

print(L)
print(L1)
print(square_dict)



 
