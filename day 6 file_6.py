'''
s1 = input("enter the string: ")
fst = s1[0].upper()
lst = s1[-1].upper()

print(fst+s1[1:len(s1)-1]+lst)

#print(s1.replace('h', 'H'))
#print(s1.replace('d', "D"))


# Eg:2

n = int(input(" enter number : "))
temp = n
f1 = 0
while n!= 0:
    rem = n%10
    check = temp%rem
    if check!=0:
        f1=1
    n=n// 10   
if f1==0:
    print("YES")
else:
    print("N0")
'''
l1 = [8,9,0,7]
l2 = [7,6,5,4]

for val in range(len(l1)):
    print(l1[val]+l2[val])

l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]

#print(l1[0]+l2[0], l1[1]+l2[1])
l3 = []
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)

# ! ---> Set

# ? characteristics of elements
#1.) set can be create using{}
#2.) the elements set are not indexed
#4.) it unorderd
#5.) heterogenous
#6.) mutable or changable

# Eg:1
s1 = {9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)

#Eg:2
#s2 = {5,8,98,[9,0]}
#print(s2) ---> error

#Eg:3
#min(), max(), len()

#Eg:4
# ? to add element inside set

s1 = {8,78,67,'u'}
#add()
s1.add(43)
print(s1)

#update()
s1.update([9,0])
print(s1)

# ? to delete element inside set
s1 = {8, 78, 67, 'u'}

#pop() ---> to delete one element randomly
s1.pop()
print(s1)

#remove()
s1.remove(78)
print(s1)

#discard()
s1.discard(67)
print(s1)

# clear()
l1 = {}
print(type(l1)) #---> datatype is dict

# s1 = set() # to create empty set
print(type(s1))

#s1 = {8,9,0}
s1.clear()
print(s1)

#del s1
#print(s1)

# join the sets
s1 = {9, 0, 8}
s2 = {9.90, "card", 't', 56}
#union() ---> to combine 2 sets
s3 = s1.union(s2)
print(s3)

# intersection() ---> to get common elements inside set
s1 = {4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.intersection(s2))

#difference
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))

#isdisjoint(), issubset, issuperset()

s1 = {8,9,0}
s2 = {6,7,5,8,9,0}

print(s1.issubset(s2))
print(s2.issuperset(s1))

# ! ---> Problem:1
s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}

#n1 = {1,2,3} #--->s1
for val in s1:
    if val in s2:
       str = "its  jointset"
print(str)

# ! ---> dictionary
#Eg:1
d1 = {1:100, 'a':200, 4.5:"hello"}
print(d1)
print(len(d1))

# ? Char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key, value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed, duplicate value are allowed
# 5.) It is unindexed
# 6.) It is ordered
# 7.) Key does not allow mutable datatypes, values allow mutable

d1 = {1:100, 2:200, 3:300, 4:400}
# to access element in dictionary

print(d1)
#or
# To access the values
print(d1[1]) #o/p --->100

# ? some common functions
#len(),min(),max()
print(min(d1))
print(max(d1))

# ? To find min, max based on values
print(min(d1.values()))
print(max(d1.values()))

# ? dictionary based functions
# to add elements(key and value pair) in dict
d1 = {1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)

# ? To replace a value in dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d1[2]="mango"
print(d1)

# ? delete element from dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
#popitem ---> to delete last key value pair in dict
d1.popitem()
print(d1)
print(d1.popitem())

#pop()
d1.pop(2) # 2 is the key in dictionary
print(d1)

#clear(), del
#update()
#join 2 dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d2 = {"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)

#get() ---> used to get the value from a key
d1 = {1:100, 2:200, 3:300, 4:400}
#print(d1[3])
#print(d1[90])
print(d1.get(90))


#to print all the keys
print(d1.keys())
print(type(d1.keys()))

#to print all the values
print(d1.values())

#Iterating dictionary
for val in d1: # to iterate keys alone
    print(val)

# for val in d1.values(): # to iterate values alone
#   print(val)

# to get both key and values
for  key, val in d1.items():
    print(key,val)

# ! Problem:1
'''
# ! problem:1

n = int(input("Enter the value: " ))
integer=[]
float_value =[]
string=[]

for val in range(n):
    value = eval(input("enter the values: "))
    if type(val)==int:
        integer.append(val)
    elif type(val) == float:
         float_value.append(val)
    elif type(val)== str:
        string.append(val)
    else:
        print("p1s provide data in int, float, string")      
print(integer)        
print(float_value)        
print(string)
'''
# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}

# ! problem:2
# return a set elements present in set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)

print(set3)


# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']

#!------> problem 3
l1=[1,2,3,4] # key
l2=["a", "b", "c", "d"] # value

#{1:'a'}
d1 = {}
for val in range(len(l1)):
    d1[l1[val]]=l2[val]
print(d1)

# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}

# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']
