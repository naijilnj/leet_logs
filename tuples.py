mytuple = (2,465,78,3.14,["Pikachu","Charmander"])
print(mytuple)

print(mytuple[0:4])

print(mytuple[4])

n_tuple=mytuple+(3,5,3,8,5)
print(n_tuple)

print(n_tuple*2)

print(len(n_tuple))

m_tuple = (mytuple,mytuple[0:4])
print(m_tuple)

print(m_tuple[1][0])

print(mytuple.count(78))

mylist = list(m_tuple)
print(mylist)

ctuple = tuple(mylist)
print(ctuple)