def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

print("8th Fibonacci number:", fibonacci(8))

#---> or

num = 8
n1 = 0
n2 = 1

for val in range(num):
    ans = n1+n2
    n1 = n2
    n2 = ans
print(ans)    

s1= "Hello how are you"
s2="Hello how is"
s1=s1.split(" ")
s2=s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)


# constructors
# ? Eg:2
# * unjparametarised constructor
class profile:
    def __init__(self):
       print("hello world")

obj = profile()

obj.__init__()

# ? Eg:3
# * Parametarised constructor
class profile:
    def __init__(self,id,name,age):
        print(id,name,age)

obj = profile(1, "hari",21)

# Eg:4
class c1:
    name = "hari"
    place = "btech"

    def m1(self):
        print(self.name,self.place)

object = c1()
object.m1()

# ? Eg:5
class c1:
    def m1(self):
        name = "hari"
        age = 21
        return name,age
    def display(self):
        # ! print(name,age)
        # ! print(self.name,self.age)
        print(self.m1())

object = c1()
object.display()

# ? Eg:6
# ? To use the variable inside the constructor in another methods 
class class1:
    def __init__(self):
        self.name = "hareesh"
        self.email = "hareeshpeetla4046@gmail.com"
        # return name,email #error ---> cannot use return with constructor

    def display (self):
         print(self.name, self.email)

c1 = class1()
c1.display()

# ! ---> Inheritance
# The process of utilising the methods and attributes of parent class
# throught the object of child class it is called as Inheritance

# 5 types of Inheritance
#Single Inheritance
#Multilevel Inheritance
#Multiple Inheritance
#Hybrid Inheritance
#Heirarichal Inheritance

# * Single Inheritance
# ? It has only one parent class and only one child class
# ! Eg:1
# ! Eg:1

class parent:
    def m1(self):
        print("Iam parent class")

class child(parent):
    def m2(self):
        print("Iam child class")

obj=child()
obj.m1()


# ! Eg:2

class c1:
    def _init_(self):
        print(" I am constructor from parent class")

class child1(c1):
    pass

obj= child1()



# ! Eg:3

class parent:
    name = "sai"

class child(parent):
    name = "name1"

    def display(self):
        print(self.name)

d = child()
d.display()

# ! Multilevel inheritance
# ? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices ")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("meow")


class parrot(cat):
    def parrot_voice(self):
        print("speak")
        
all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()

'''
# ? Eg:2
class honda_city:
    def honda_city_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def honda_city_body_specs(self, color, weight, height, length, vehical_type):
        print(color, weight, height, length, vehical_type)

class civic(amaze):
    def civic_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def civic_body_specs(self, color, weight, height, length, vehical_type):
        print(color, weight, height, length, vehical_type)

class amaze(Honda_city):
    def amaze_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def amaze_body_specs(self, color, weight, height, length, vehical_type):
        print(color, weight, height, length, vehical_type)

class Honda(civic):
    pass

honda = Honda()
honda.honda_city_engine_spec(1500,230,2979,"petrol",4)
honda.civic_body_specs("white",2000,5.5,8,"Hatchback")
'''

# Multiple Inheritance
 #? It has multiple parent and 1 child
class white_pertol:
    def function_w(self):
        print("used to Airplans")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol(white_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
p=petrol()
p.defanition()
p.function_o()


# ! Eg:2
# MRO ---> Method resolution order

class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)

'''
# ! Heirarichal Inheritance
# ? The one parent class will acts as parent for all child classes
class catagory:
    def weight(self, weight):
        print(weight)

    def display(self,color,taste):
        print(color,taste)

class Tomato(catagory):
     def tomato_specs(self):

     color = "black"
     taste = "neutral taste" 
     self.display(color,taste)
    
class carrot:
    def carrot_specs(self):
        color = "green"
        taste = "sweet"

c = carrot()        
c.carrot_specs()
c.weight("30gms")

t = tomato
t.tomato_specs()
t.weight("20gms")
'''

# ! Hybrid inheritance
# ? The combination of above 4 inheritance is called Hybrid inheritance

class c1:
    def m1(self):
        print("class 1")

class c2(c1):
    def m2(self):
        print("class 2")


class c3(c2):
    def m3(self):
        print("iam m3 from m4")

class c4(c2):
    def m4(self):
        print("class 4")
        
class c5(c3):
    def m5(self):
        print("class 4")
        
class c6(c5, c4, c2, c1):
    def m6(self):
        print("class 4")
        
obj = c6()
obj.m3()


# ! -------> Polymorphism
# Poly - many, morph --> form
# A function which has the ability to perform more than 1 functionality
# then it is considered to be as polymorphism

# * Polymorphism in built in functions
# len() --> which is used to find the length of list, tuple, dict ect..
# index()
# max()
# min()
# count()
# pop()
# and more...

# * Polymorphism in operators
# +
print(8+8)
print("k"+"l")
print([1,2,3]+[5,6])

# *
# print(6*7)
# l1 = {12,2,3,4}
# print(*l1)
# def f1(*args):
# l1 = [1,2,3,4]
# print(l1*10)


# Polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading --> it is not possible in python
# 2.) Method overloading

# 1.) Tasks

# write the code for the below tasjs using function
# 1.)d1 = {"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
# a.) Find the min ans max priced product
# b.) Find the product starts with "s" and "S"

# 2.) Find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6]
# n=2 --> [5,6, 1,2,3,4]
# n=3 --> [4,5,6, 1,2,3]
