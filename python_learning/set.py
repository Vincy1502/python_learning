v1={1,2,"hello",2,True}
print(v1)

v2={0,False}
print(v2)

v3=list(v1)
print(v3.index("hello"))
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

c={"a","b","c","a","a","b"}
d={1,2,3,2,3,3,4}
f=c.union(d)
print(f)

# e=c|d
# print(e)


m={1,2,1,4,6,"a","b"}
n={1,5,6,"a","b","c"}
o=m.intersection(n)
print(o)

m1={1,2,3,"a","b"}
m2=[1,"a","b",5,6,"a",2]
m3=m1.intersection(m2)
print(m3)

# m1.intersection_update(m2)
# print(m1)

m3=m1.difference(m2)
print(m3)

m3=m1-d
print(m3)

m3=m1^d
print(m3)


