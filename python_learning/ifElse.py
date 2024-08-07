
#conditional statement
a = 10
b = 10
c=20

#if condition used  for comparition
if a==b:
    print("a is equal to b")
else:
    print("a is not equal to b")    

if a>b:
    print("a is greater than b")
elif a==b:
    print("a and b is equal")  
elif a<b:
    print("a is less than b")  
else:
    print("a is not equal to b")    

#short hand if and if else
if a>b: print("a is greater than b") 
else: print("a is less than b")   

print("a is greater or equal") if a>=b else print("equal") 

x=5
y=10
z=15

if x > y and x > z:
    print("x is greater than y and z")
else:
    print("x is less than y and z")

#pass statement for pass the condition to the else 

if x>10:
    pass
else:
    print("10 is greater")

#looping statement(iteration)

l1=["a","b","e","f","c","g"]

# i=0
# for i in range(len(l1)):
#     if l1(i)=="c":
#        print(i)

for i in range(len(l1)):
    n="c"
    m=l1[i]
    if n==m:
        print(i)

for i in range(len(l1)):
    v=l1[i]
    print(v)
    if v=="f":
        break

for h in l1:
    print(h)   
    if h=="f":
        break

#for not declaring staring and ending
#while declaring starting and ending

prime=[]
ntprime=[]
num=int(input("enter the number")) #18

if num==1: #18==1 false
    print("not prime") 
elif num>1: #18>1 true
    for i in range(2,num): #5
        if num%i==0:#18%2==0,5%3==0,5%4==0 
            print("not prime")
            break
        #    for i in range(2,num+1):
        #        print(i)
    else:
        print("prime")

else:
    print("not prime")
               
           



   