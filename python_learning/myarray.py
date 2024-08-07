v=["a","b","a"]
print(type(v))

# import array as arr

# v1=arr.array('i',[1,2,3]) #i for integer signed int
# print(v1)

# v2=arr.array("I")

from array import *
v2=array('i',[1,2,3,4,5])
for i in range(len(v2)):
    b=v2[i]
print(v2.buffer_info())

x=10
print(id(x))

v4=array(v2.typecode,(a  for a in v2))
print(v4) #typecode for copy

vin=array('i',[])
name=int(input("enter the length:"))
for n in range(name):
     j=int(input("enter the values"))
     vin.append(j)
print(vin)

#task---find the position supose not wrong supose duplicates in the array it will print second tym accure

v3=array('I',[1,2])
print(v3)


def funcName(*a1):# parameters
     print(a1)
     print(a1[2])
funcName(12,20,30,50)#arguments

def vincy(x,y):#variales
    z=x+y
    c=x-y
    return z,c #execute the task dont print
g,h=vincy(5,7) #values
print(g,h)
