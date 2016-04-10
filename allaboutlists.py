list1= ['chelsea','manu','mancity','arsenal','liverpool']
#I can do this, a list of all strings

list2= [1,2,3,4,5]
#I can do this, a list of integers or floats

list3= ['chelsea',1,'manu',2,'arsenal',3]
#I can even mixmatch a list containing integers and strings

list4= ["aston villa","sunderland","newcastle","norwich"]
#"double-quotes or single quotes doesn't matter"

list5 = [1,]
#trailing comma necessary for the lone ranger

print list1
print list2
print list3
print list4

print list1[0]
#I can display the first element like this .. everyting starts with a zero..

print list2[3]
#and then any other

#Slicing
#Selectively pick out a range of elements
print list2[1:3]
print list2[0:5]
print list2[2:]

#Assignment
#Assign a value to a list index
list2[2] = 234;
print list2

#Deletion
#Delete an element from the list or dump the entire list in the trash..
del list2[3]
print list2

#Length
#So how long is your list?
len(list2)
len(list5)

#Concatenate
#
list5 = [1,2,234,5]
print list2 + list5

#Repitition
#
>>> [1,]*4
[1, 1, 1, 1]

#Membership
#True or False
>>> 1 in list1
False
>>> 1 in list2
True

#Iteration
for x in list2:
  print 2*x


>>> list3 = [0,]*4
>>> list3
[0, 0, 0, 0]
>>> for x in range(0,len(list2)):list3[x]=list2[x]
...
>>> list3
[1, 2, 234, 5]

#Compare
cmp(list2,list3)
cmp(list1,list2)

#Max and Min
max(list2)
234
>>> min(list2)

#append
list2.append(list3)
print list2
print list2[4]
print list2[4][2]

#count
list6 = [1,1,1,1,3,3,4,4,4]
print list6.count(1)
print list6.count(2)
print list6.count(3)
print list6.count(4)

#extend
list2.extend(list6)
print list2

#lowest index
print list6.index(1)
print list6.index(4)
print list6.index(3)

#insert object
list6.insert(2,2)
print list6
list7 = [1,234,56,78]
list6.insert(3,list7)
print list6

#pop
print list6
list6.pop(3)
print list6
list6.pop(2)
print list6

#remove
list2.remove(1)
print list2
list2.remove(234)
print list2
list2.remove(1)
print list2
list2.remove(4)
print list2

#reverse
list6.reverse()
print list6
list6.reverse()
print list6

#sort
list2.sort()
print list2

list7 = [5,6,987,0]
list2.insert(3,list7)
print list2
list2.sort()
print list2
list8 = [1,2,113,5]
list2.insert(3,list8)
print list2
list2.sort()
print list2










