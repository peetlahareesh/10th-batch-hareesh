'''
#--->while loop
#--->break using while loop

# Eg:1
# 1.)Iterate from 20 to 30 and break the loop in 27
#-->ANSWER
i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1
# 2.)
i = 20
while i<31:
    print(i)
    i+=1
    if i ==27:
        break

# 3.)
i = 20
while i<31:
    print(i)
    if i ==27:
        break
    i+=1

# ! ----> continue
i = 20
while i<31:
    if i ==27:
        continue
        print(i)
    i=i+1

#Eg : 5
#while to iterate from 12 to 22
# find the sum of all numbers

i =12
sum=0
while i<23:
     sum=sum+i
     print(sum)
     i+=1
     


i=12
add=0
while i<=23:
    add+=i
    i+=1
    if i==23:
        print("sum of number is:",add)

# ! Eg :1
# Find the average of value from 20 to 25
# Initialize variables

i=20
sum=0
count = 0
while i<=25:
    sum = sum+i
    count+=1
    i+=1
print(sum/count)

# ! ----> Nested for loop
# Eg:1

for i in range(1,3):
    for j in range(1,4):
        print(i,j)


#Eg:2
# * * * *
# * * * *
# * * * *
# * * * *

rows = int(input("enter the rows: "))
cols = int(input("enter the cols: "))

for row in range(rows):
    for col in range(cols):
        print("*", end=" ")
    print()

for row in range(5):
    for col in range(5):
        sum= sum+1
        print(sum, end=" ")
    print()

# ! to print stars in right angled triangle

for row in range(0,25):
    for col in range (0, row):
        print("*", end=" ")
    print()   

#Eg:3
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# * 
rows = 6
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print("\n")

#*****
#*   *
#*   *
#*   *
#*****
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#      *
#    * * *
#   * * * *
#  * * * * *
for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
#*
#* *
#*   *
#*     *
#*       *
#* * * * * *             
for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

# ! ---> List types

# ! ---> Data types
# Primary

#Number
#String
#Boolean
#None

#Collection
#list
#tuple
#Set
#Dictionary


# ? ---> List

#1.) if the collection of elements are surrounded by square brackets, it is considered
# to be list
# ! Eg:
    # l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8,9,0]]

#characteristics of list
# 1.) list have to be surrounded by[]
# 2.) It is mutable (the elements in the list are changeble)
# 3.) Every element inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous
    
# To access the elements in list
lst1 = [1,4,1,7,89,7,5,"p","i"]
print(lst1)

# ---> Indexing
#In the collection datatypes like list,tuple,string,the elements will be alloted
# with pre-defined unique value called index value

#wwe have 2 types of indexing
# positive indexing ---> starts with 0 from left hand side
# negative indexing ---> starts with -1 from right hand side

# ? --->Positive Indexing
#lst1 = [1,4,1,7,89,7,5,"p","i"]
#print(lst[0])
#print(lst[4])
#print(lst[20]) --->error

# ? ---> Negative indexing
#lst1 = [1,4,1,7,89,7,5,"p","i"]
#print(lst[-1])
#print(lst[-5])

# ? ---> slicing
lst1 = [1,4,1,7,89,7,5,"p","i"]
#lst[start_index:end_indexstep]

print(lst1[0:4])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])

#print(lst1[0:7:1]) # lst1[0:7] --->both are same
print(lst1[0:7:2])

'''

#trail = int(input())

lst1 = [1,4,1,7,89,7,5,"p","i"]
#print(lst1[-4:-1])
#print(lst1[-1:-4]) --->[]
#print(lst1[-7:-1])
#print(lst1[-7:-1:2])

# ! To insert of add element inside list

# append()  --> used to add element at last position of list
l1 = [9,8,0,6]
l1.append("car")
print(l1)
