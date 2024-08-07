s=("a","b","c",1,2,1,3,"a","a")

#for count the values
print(s.count("a"))

#index method for find the position of the value
print(s.index(1))

s1=("earth",)
print(type(s1))

d=list(s1)
d.append("moon")
s1=tuple(d)
print(s1)

d=list(s)
d.remove("b")
s=tuple(d)
print(s)

d=list(s)
d.pop(3)
s=tuple(d)
print(s)

# del s1
print(s)

d=list(s1)
d.clear()
s1=list(d)
print(s1)

a,b,c,*e=s
print(a)
print(b)
print(c)
print(e)

