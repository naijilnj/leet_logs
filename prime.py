#SK
#n = int(input("Enter a number: "))
#count=0
#for i in range(1,n):
#    print(i,n%i)
#    if n%i==0:
#        count+=1
#
#if count>2:
#    print("not prime")
#else:
#    print("Prime")

n = int(input("Enter a number: "))

for c in range(2,n):
    if c<n:
     if n%c==0:
      print("Number is Not Prime")
      break
     c+=1
    print("Number is Prime")
    break
