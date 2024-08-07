tuple2=(1,2.0,"vincy")
print(tuple2)

print(tuple2.count(1))
print(tuple2[2])

#index method for find the position of the value
print(tuple2.index("vincy"))

rare=("hello",)
print(rare)
print(type(rare))

tuple1=("van","car",1,2,3)
a=list(tuple1)
print(a)
a[1]="bus"
b=tuple(a)
print(b)

c=list(b)
c.append("home")
b=tuple(c)
print(b)

tuple3=tuple1+b
print(tuple3)

g=("erode",)
tuple3+=g
print(tuple3)

d=list(tuple3)
d.pop(3)
tuple3=tuple(d)
print(tuple3)

tuple4=("g","h","i","j","k","i","j")
x,*y,z=tuple4
print(y)
print(x)
print(z)

for m in tuple4[0:5]:
    print(m)

for f in tuple4:
    print()
    
for k in range(6):
    print(k)

l=tuple4*2
print(l)

n=0
while n<len(l):
    print(l[n])
    n+=1










