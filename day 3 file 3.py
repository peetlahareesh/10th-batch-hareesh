# ! Eg:3
# ? Take values of length and breadth of a
# ? from user and check if it is square or not

#length = int(input())
#breadth = int(input())
#if length==breadth:
#    print("its a square")
#else:
#    print("its not a square")

# ! Eg:4
# Python program to check whether the
# given integer is a multiple of both 5 and 7

#n=int(input("enter the number: "))
#if n%5==0 and n%7==0:
#    print("yes")
#else:
#    print("no")


# ! Eg:5
# write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to the following criteria :

#       cost price (in Rs)                                Tax
#       >100000                                            15 % + discount 6%
#       >50000 and < = 100000                              10%
#       <50000                                             5%


#price = int(input("enter the price"))
#amount = 0
#if price >=100000:
#   discount = price*(6/100)
#   value = price-discount
#   amount=value*(15/100)
#   total = value+tax
#else:
#    tax = price*(5/100)
#    total = price+tax
#print("The onroad cost of bike is: ",total)            
            
# if elif
# Eg: 1
#a=7
#b=9
#c=3

#if a >b and a<c:
#    print("A is greater")
#    print("B is greatrer")
#elif c>a and c>b:
#    print("C is greater")


#A school has following rules for grading system
# a.below 25 - F    
# b.25 to 45 - E
# c.45 to 50 - D
# d.50 to 60 - C
# e.60 to 80 - B
# f.above 80 - A
# Ask user to enter the marks and print the corresponding grade

#mark = int(input("enter the mark:"))
#if mark>=80 and mark<=100:
#    print("A")
#elif mark>=60 and mark<80:
#    print("B")
#elif mark>=50 and mark<60:
#    print("c")
#elif mark>=40 and mark<50:
#    print("D")
#else:
#     print("fail")

# ! --> short hand if else
#Eg:1
#a=9
#b=60
# if a>b:
#    print("A")
#else:
#      print("B")
#? ---> using short hand if else
# *Rules
# 1.) statement inside the if condition have to be present at first
# 2.) elif cannot be used in short hand if else
# 3.)   Always it have to end with else

# print("A") if a>b else print("B')
#


# ! code to check the givenn char is vowel or consonent
#char=input("enter the char: ")
#if char=="a" or char =='e' or char =='i' or char=='o' or char=='u':
#else:
#    print("is a consonent")
    
# ? or
# str1 = "aeiouAEIOU" 
# if char in strl:
#     print("vowel")
#else:
#    print("consonant")

# ! shorthand if else
#char = input("Enter the char: ")
#print("vowels") if char in strl else print("consonant")


# ! --> elif laddeer using shorthand if else
# Eg:1
# ? find greatest among 3 variables using short hand if else
#a=8
#b-5
#c=9

#print("A is greater") if a>b and a>c else print("B is greater")
#if b>a and b>c else print("C is greater")


# ! ---> Looping

# looping can be implimented using
# for loop
# while loop

# ---> for loop
# ? for loop is used for iteration,if we know the numner of times the loop have to run
# ? It is used to iterate the iterables eg(string,list,tuple,etc...)


#todo ---> Syntax for loop
#for syntax in c:
#for(i=0;i<10;i++){
#    printf("hello");
#}


# ! for syntax in python
# for userdefined vaariable in range(start,end,step):default step value is 1
# statement
# statement
# statement

# ? Eg:1
#to print the value from 1 to 10 using for loop

#for i in range(0,1000):
#    print(i)

# ? Eg:2
#for val in range(1, 10, 2):
#      print(val) 

#for val in range(1, 10, 3):
#      print(val)

# ? Eg:3
# to decrement the value

#for val in range(10,0,-1):
#      print(val)


#for val in range(10,0,-2):
#      print(val)       

#for val in range(1, 10, 1):
#      print(val) 

# ? Eg:4
# ! print the output of 7th multiplication table 21 to 43
#for val in range(1, 30+1):
#    print('34','x',val,'=',val*34) #--->method:1

#    ans="7x{}={}"
#    print(ans.format(val, val*7))  #---->method:2
#    print(f"7 x {val}={val*7}")    #---->method:3

# ? Eg:5
# break ---> used to terminate the loop

# for val in range(1, 10):
#     if val ==6:
#         break
#  print(val)

# ? Eg:6
#for val in range(1, 100):
#    print(val)
#    if val ==98:
#        break

#Eg:7
#for val in range(1, 10):
#    if val ==6:
#        print(val)
#        break

# ! continue
# Eg:1
#for val in range(1, 1000):
#    if val ==6:
#        continue
#    print(val)

#for val in range(1, 30):
#    if val == 6 or val == 8 or val ==21:
#        continue
#    print(val)

# ! Practise problems
# ? Print the even number between 20 to 40
#for val in range(20,41):
#    if val %2==0:
#        print(val)

# ! -----> while loop
#while is used when we do not know the number of times the loop have to run
# ? to iterate the non iterable elements while loop is used


# todo syntax

#intialisation
#while condition:
# statement
# incre or decre

#Eg:1
# to iterate number from 1 to 10

#i = 0
#while i<11:
#    print(i)
    
# for loop practise
# write a program to diaplay sum of odd numbers and even
# numbers that fall problem
# 12 and 37(including both numbers)


# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Print the reverse of given number --> n1= 234 o/p --> 432


#1st answer
def catAndMouse(x, y, z):
    dist_cat_a = abs(z - x)
    dist_cat_b = abs(z - y)
    if dist_cat_a == dist_cat_b:
        return "Mouse C"
    elif dist_cat_a < dist_cat_b:
        return "Cat A"
    else:
        return "Cat B"
# Example usage
print(catAndMouse(1, 2, 3))  # Output: Cat B

#  2nd answer
num = 8
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)

# 3rd answer
sum_even = 0
sum_odd = 0
for num in range(12, 38):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)

# 4th answer
n1 = 123
total = 0
while n1 > 0:
    digit = n1 % 10
    total += digit
    n1 //= 10
print("Sum of digits of the number:", total)

#5th answer
n1 = 234
reverse = 0
while n1 > 0:
    digit = n1 % 10
    reverse = reverse * 10 + digit
    n1 //= 10
print("Reverse of the given number:", reverse)
