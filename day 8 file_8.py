# ! Eg:3
def profile(name,age,place):
    txt ="My name is{}.Iam{}years old. Iam from{}."
    print(txt.format(name,age,place))
profile("hareesh", "21", "pulivendula") 


# ! Eg:4
# ? Function with return statement

# return
#1.) A variable declared inside the function can be accessed outside
# the function using return
#2.) return does not print anything
#3.) we cannot write any code below return statement


#def f1():
#    z = 8
#f1()
#print(z) # error ---> cannot use outside the function


def f1(a,b):
    c = a*b
    return c
# print(f1(6,8))
obj = f1(6,8)
obj1 = f1(4,6) 


def gracemark(object):
    print(object+4)
gracemark(obj)    
gracemark(obj1)

'''
#123
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
         print(n, "Palindrome")
    else:
         print("Not palindrome")         
a = int(input("Enter the value:"))
palindrome(a)    
'''

# ? Based on the declaration of parameter and args
# ? function are divided into 5 catagories

# Positional args
# keyword args
# default args
# variable length args
# keyword variable length args

# * Positional args
# ? The position of parameter have to be same as psotion or arguments
# Eg:1
def profile(name,phone,mark):
     txt = "My name is {}. My phone number is{}.I got {} marks."
     print(txt.format(name, phone, mark)) 

profile("Hareesh", "7702235254", "95") # unexpected output

# * Keyword args
# ! Eg:1
# ? To overcome the disadvantage of position args, we use keyword args
# ? It is the process of intialising the parameter with the args while calling
# ? the function
def profile(name,phone,mark):
     txt = "My name is {}. My phone number is{}.I got {} marks."
     print(txt.format(name, phone, mark)) 

profile(name = "Hareesh", phone = "7702235254", mark = "95") # unexpected output


# todo ---> Exception of keyword args function
def profile(name,phone,mark):
     txt = "My name is {}. My phone number is{}.I got {} marks."
     print(txt.format(name, phone, mark)) 
# profile(name="hareesh",7702235254,mark=98) #error ---> positional args follow keywordargs
# profile(7702235254, name="hari", mark=98)  #error ---> name has multiple values
profile("hareesh", mark=95, phone=7702235254)


# * Default args
#The method of asssigning the argument to the parameter while declaring the function 
# ! Eg:1
def profile(name,phone,place="kadapa"):
     txt = "My name is {}. My phone number is{}.I am from {}."
     print(txt.format(name, phone, place))

profile("hari",7213132135)     

'''
Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal
'''

# * Variables length params
# ! Eg:1
# To pass more then 1 arg to a parameter means we use variable length args
# To convert normal parameter to variable length param,add * to their prefix of param

#name = "hareesh", 'name2', 'name3'
def profile(*name):
    for val in name:
        print("My name is",val)
profile("hari",'name2','name3')    

#Keyword variable length args
# kwargs ---> which is used to provide the args in the form of key vlue pair
# ! Eg:1

def price(**price_list):
    print(price_list)

price(shirt=1000, iphone=80000)


#n=5
#{1:1, 2:4, 3:9, 4:16, 5:25}

def generate_dict(n):
    return {x: x*x for x in range(1, n+1)}

n = 5
print("Sample Dictionary (n =", n, "):")
print("Expected Output:", generate_dict(n))
'''
n = int(input("Enter the number:"))
d1 = {}
for val in range(1, n+1):
    d1[val] = val**2
    print(d1)
'''    
d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200, c=300)

print(d1)


def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val] = val**2
    print(d1)
dict1(5)



# ! ---> object oriented programming

# The paradigms of objects oriented progarmming are


# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! Class is a blue print of an object
l1 = [1,2,3,4,5,6]

# ? Eg:1
class c1:
    name1 = "hareesh"
    print(name1)

# ? Eg:2
class person:
    name = "hareesh"

# c = person() # c as object
# The name of creation of an object is called as method
# print(c.name)
    
# ? Eg:3
# create of a method
# when the function is created with a class is called as method

class person:
    def display(method): 
        print("Hello welcome to classes")


p = person()
p.display()

# ? Eg:4
# ! Method with parameter
class person:
    def display(person, name, age):
        print(name,age)
p = person()
p.display("hareesh", 21)


# ! Eg:5
class person:
     fname = "hareesh" #attribute or static variable
     lname = "Peetla"
     
     def first_name(self):
         print(self.fname)

     def full_name(self):
         print(self.fname+" "+self.lname)
 
p = person()
p.first_name()
p.full_name()

# ? Eg:6
# constructors ---> __init__()
# This is a special method which has the ability to execute itself without
# calling it manually through the process of instatiation

class profile:    
    def __init__(self):
        print("hey")

p = profile() # execution through this process
p.__init__()

#1.) Write a Python script to generate and print a dictionary that
#contains a number (between 1 and n) in the form (x, x*x). Sample Dictionary (n=5):
# Expected Output (1:1, 2:4, 3:9, 4: 16, 5:25)
#2.) Find the uncommon words from 2 strings
# s1 "Hello how are you"
# s2 "Hello how is"
#3.) Write a code print the 8th fibanochi number
