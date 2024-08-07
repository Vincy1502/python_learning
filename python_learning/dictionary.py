dict1={"name":"vincy","year":2004,"deg":"bca","skill":["html","css","python"]}
print(dict1)

print(dict1["year"])

print(len(dict1))

print(type(dict1))

x=dict1.get("deg")
print(x)

x1=dict1.keys()
print(x1)

dict2={"name":"vincy","year":2004,"deg":"bca","skill":["html","css","python"]}
print(dict2.keys())
dict2["color"]="red"
print(dict2.keys()) #view

print(dict2.values())

print(dict2.items())

if "name" in dict2:
    print("yes name is present")
#add items 3 ways
dict2["year"]="2005"
print(dict2)

dict2.update({"year":"2004"})
print(dict2)

dict2.update({"work":"training"})
print(dict2)

#remove 
dict2.pop("work")
print(dict2)

dict2.popitem()
print(dict2)

# del dict2

del dict2["skill"]
print(dict2)

#clear dict2

#copy values
dict3=dict2.copy()
print(dict3)

dict4=dict(dict3)
print(dict4)

#nested dict
dict5={"dict1":{1:"a",2:"b"},"dict2":{"name":"vincy","year":2004,"deg":"bca","skill":["html","css","python"]}}
print(dict5)




