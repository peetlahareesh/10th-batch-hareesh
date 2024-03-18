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


# ! ---> 1st Answer
d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
d1.update(d2)
print(d1)


# ! ---> 2nd Answer
set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c = 0
set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c = 0
flag = 0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break

    if c==3:
        for val in set3:
            if val in set2 or val in set3:
                flag=1
                break

if flag==0:
    print("Disjioint")
else:
    print("joint")
                

# ! ---> 3rd Answer 

# O/P --> ['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = []
i = 0
while i < len(list1):
    combined_string = list1[i] + list2[i]
    result.append(combined_string)
    i += 1
print(result)

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

l3=[]
i = 0

while i < len(list1):
    l3.append(list1[i] + list2[i])
    i += 1

print(l3)

# Hacker rank ---> Caesar Cipher

# ! Functions
# Def
# Function is a block of code which is used to perform a specific
# functionality
# Function can be created using def keyword

# Function has 3 parts
# Function declaration
# Function defination
# Function call


#def greet():
#    print("Greetings User!!")

#greet() # function calling    


# ! Eg:2
#def adding():
#    d = a+b+c
#    print(d)
#adding()
#adding()

# ? Function with parameter
'''
def greeting(name):
    print("Welcome",name)

for val in range(3):
     username = input("Enter the name:")
     greeting(username) #username is argument
'''
# ! Eg:3
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number

# ---> 1st answer
def generate_squared_dict(n):
    squared_dict = {}
    for x in range(1, n + 1):
        squared_dict[x] = x * x
    return squared_dict

# ---> 2nd asnwer
n = 5
result_dict = generate_squared_dict(n)
print("Expected Output:", result_dict)

def find_uncommon_words(s1, s2):
    words1 = set(s1.split())
    words2 = set(s2.split())
    uncommon_words = words1.symmetric_difference(words2)
    return uncommon_words
# ---> 3rd answer 
s1 = "Hello how are you"
s2 = "Hello how is"

uncommon_words = find_uncommon_words(s1, s2)
print("Uncommon words:", uncommon_words)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

n = 8
result = fibonacci(n)
print("The 8th Fibonacci number is:", result)


