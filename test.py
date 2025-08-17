#n = int(input("Enter a number: "))
#k = str(n)[::-1]
#
#
#if str(n) == k:
#    print('Palindrome',k)
#else:
#    print('Not Palindrome',k)


n = input("Enter a number: ").lower()

if n == n[::-1]:
    print('Palindrome',n)
else:
    print('Not Palindrome',n)

