n = int(input("Enter a number: "))
new = str(n)
k=0

for i in new:
    k += int(i) ** len(new)

if k==n:
    print("Armstrong")
else:
    print("Not Armstrong")
