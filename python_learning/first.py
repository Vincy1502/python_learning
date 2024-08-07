print("hello world")
x=10
y=25
x=35

a="hello"

def func():
    return "hii"
func()    
 
def name():
    b = func()
    print (b)
name()

def funcName():# parameters
    b= func()
    print (b)
funcName()#arguments

#type convertion
x=100
print(type(x))
y=float(x)
print(y)
print(type(y))


import random
print(random.randrange(1,100))

c=int(2.8)
print(c)
print(type(c))

d="""Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quaerat ratione assumenda expedita voluptatum quidem voluptas "saepe minus officiis" tempore ipsam laudantium accusamus, suscipit, vel ipsum commodi rerum eum nobis nisi"""
print(d)

e="hello world"
print(e[3:])

for f in "python":
    print(f)

g="welcome to python!"  
print(len(g)) 

text="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quaerat ratione assumenda expedita voluptatum"
print("ratione" in text)

slicing="programming language"
print(slicing[12:16])

h="my name is vincy"
print(h.split("is"))

z="welcome to home"
y="enjoy"
w=z+ " " + y
print(w)

i=5
j=2
total=i+j
print(total)

