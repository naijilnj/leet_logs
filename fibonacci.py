n = int(input("Enter a number: "))
a=0
b=1

for i in range(n):
     print(a) #1
     temp=a+b #3
     a=b #2
     b=temp #2

