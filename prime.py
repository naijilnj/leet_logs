#SK
n = int(input("Enter a number: "))
count=0
for i in range(1,n):
    print(i,n%i)
    if n%i==0:
        count+=1

if count>2:
    print("not prime")
else:
    print("Prime")