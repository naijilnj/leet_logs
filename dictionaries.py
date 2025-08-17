mydict = {'Name':'Pikachu','Type':'Electric','Evolution Level':2,'Trainer':'Ash'}
print(mydict)

print(mydict.get('Trainer'))

mydict[4] = "Season"
print(mydict)

print(mydict.keys())
print(mydict.values())

for i in mydict.keys():
    print("Keys",i)

for i in mydict.values():
    print("Values",i)

cp = mydict.copy()
print(cp)

cp.clear()
print(cp)

mydict["Trainer"] = "Ash Ketchum"
print(mydict)

del mydict["Evolution Level"]
print(mydict)
