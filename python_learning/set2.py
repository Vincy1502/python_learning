v1={"a","b","hello",1,True,0,"hii"}
print(v1)

v2={0,False}
print(v2)

a=list(v1)
print(a.index("hello"))
b=set(v1)
print(b)

print("hello" in b)

x="hello"
for x in b:
    print(x)

b.add("hii")    
print(b)

b.update(v2)
print(b)

b.discard("bus")
print(b)

b.remove("hii")
print(b)