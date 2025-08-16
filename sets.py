nset={45,78,89,34}
mset={78,90,23,45,67,34}
print('nset',nset)
print('mset',mset)

nset.add(4)
print(nset)

nset.update([67,24,78,90,343,4.56])
print(nset)

nset.discard(444)
print(nset)

nset.remove(444) #throws error
print(nset)

print('Union',nset|mset)

print('Intersection',nset & mset)

print('A-B',nset - mset)
print('B-A',mset - nset)

print('B^A',nset^mset)
