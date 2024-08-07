mylist=["erode","salem","coimbatore"]
print(mylist)
#length of the list using length method [length ---highest list index]
list1=["kavi",10,4.6]
print(list1)
print(len(list1))
#find the type of list
print(type(list1))

#print the position values
list2=["a","b","c","d","e","f","g"]
print(list2[2:6])

#check the particular value using if condition
if 'c' in list2:
    print("c is present")
else:
    print("c is not present")

#print the list values using for loop   
i=0
for x in list2:
    x=list2[i]  
    print(x) 
    i=i+1
#change the list value using the position
list2[3:]="car","bus","train","bike"
print(list2)

list2[3:4]="welcome","hello","hii"
print(list2)

list2[4]="lap"
print(list2)

list2[4:6]="van","fan"
print(list2)

#insert method for inserting the new value using position
list2.insert(4,"earth")
print(list2)

#adding the value in the last using append method
list2.append("home")
print(list2)

#adding the two list using extend method
# list2.extend(list1)
# print(list2)

list2.append('home')
print(list2)
#count the duplicates and original values using count method
print(list2.count("home"))

list2.remove("home")
print(list2)

# remove the value using position or empty
list2.pop()
print(list2)

del list2[1]
print(list2)

# list2.clear()
# print(list2)

list1.clear()
print(list1)
print(list2)

# sort method for assending order
list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)


list2.reverse()
print(list2)

list3=list1+list2
print(list3)
