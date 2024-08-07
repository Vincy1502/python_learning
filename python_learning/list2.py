vincy=[1,1.0,"tamil","english"]
print(len(vincy))
print(type(vincy))
print(vincy[0:])

print(1 in vincy)

if "tamil" in vincy:
    print("true")
else:
    print("tamil is not found")

for a in vincy:
    print(a)   

vincy[0:2]="hindi","malyalam"
print(vincy)

vincy.insert(3,"telungu")
print(vincy)

vincy.append("marati")
vincy1=[1,2,3]
vincy.extend(vincy1)
vincy.append("tamil")
print(vincy.count("tamil"))
vincy.remove("tamil")
print(vincy)

vincy.pop(3)
print(vincy)

del vincy[4:7]
print(vincy)

vincy1.clear()
print(vincy1)

vincy.sort()
print(vincy)

vincy.sort(reverse=True)
print(vincy)

vincy.reverse()
print(vincy)

v1=[1,2,3]
v3=vincy+v1
print(v3)