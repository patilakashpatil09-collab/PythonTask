# TUPLE
# mytuple=("prashant","Ashish","komal","ankush","Ashish",77,"snadip",60,90,"pratik")
# print(mytuple)
# print(type(mytuple))
# print(mytuple[0])
# print(mytuple[-1])
# mytuple[0]="prashant"  # This will cause an error because tuples are immutable but lists are mutable
# mytuple.append("prashant")  # This will also cause an error because tuples do not have an append method

# Set Data Type

# myset={"prashant","Ashish","komal","ankush","Ashish",77,"snadip",60,90,"pratik"}
# print(myset)
# print(type(myset))
# myset.add("prashant")  # This will not add "prashant" again because sets do not allow duplicate values
# myset.add("Akash") 
# print(myset)
# print(type(myset))# This will not add 53 again because sets do not allow duplicate valuesmy
# myset.discard(60)
# print(myset)
# myset.remove("prashant") # This will remove "prashant" from the set, but if "prashant" is not in the set, it will raise a KeyError
# print(myset)

# use of UNION Function in set
# myset={1,4,5,6,7}
# newset={1,2,3,4,5}
# print(myset.union(newset))
# print(newset) # This will return a new set that contains all the unique

# Intersection of two sets
# myset={1,4,5,6,7}
# newset={2,5,7,3,8}
# print(myset.intersection(newset)) # This will return a new set that contains only the elements that are present in both sets or common elements in both sets
# print(newset)

# Difference of two sets using method

# myset={1,4,5,6,7}
# newset={2,5,7,3,8}
# print(myset.difference(newset)) # This will return a new set that contains only thes
# print(newset)

myset={1,4,5,6,7}
# print(myset.pop()) # This will remove and return an arbitrary element from the set. If the set is empty, it will raise a KeyError
# print(myset)
# print(myset.add(10))
# print(myset)# This will cause an error because sets do not have a push method, but lists do have a push method (which is actually called append in Python)
# print(myset.clear()) # This will remove all elements from the set, leaving it empty
# print(myset)

# Dictonaary Data Type

# mydict={"name":"prashant","age":25,"city":"New York","country":"USA"}
# print(mydict)
# print(type(mydict))
# mydict['id']="12345"
# print(mydict)
# print(mydict["name"])

# mydict[2]="prashant"
# print(mydict)

# mydict={
#     101:"prashant",
#     102:"Ashish",
#     103:"komal",
#     104:"ankush",
#     102:"Akash"     
    
    
# }
# print(mydict) # This will show that the key 102 has the value "Akash" because in a dictionary, keys must be unique, and if you assign a new value to an existing key, it will overwrite the previous value.
# # also we can update the value of a key in a dictionary by assigning a new value to that key. For example, if we want to update the value of key 101
# mydict[101]="Prashant Kumar"
# print(mydict)

# a=mydict[102]
# print(a) # This will print the value associated with key 102, which is "Akash" because the previous value "Ashish" was overwritten when we assigned "Akash" to key 102.
# a=mydict.get(103)
# print(a) # This will print the value associated with key 103, which is "kom

# mydict[104]="snadip"
# print(mydict)

# loop in dictionary
# for x in mydict:
#     print(x) # This will print the keys of the dictionary
# for x in mydict.values():
#     print(x) # This will print the values of the dictionary

# printing both keys and values in a dictionary
# for x,y in mydict.items():
#     print(x,y) # This will print the key-value pairs as tuples in the form of (key, value)

# mydict[106]="pratik"
# print(mydict)

# mydict.pop("name")# This will remove the key 102 and its associated value from the dictionary, and return the value that was removed. If the key 102 is not found in the dictionary, it will raise a KeyError
# print(mydict)
# newdict=mydict.copy()
# print(newdict)


# for i in range(1,5):
#     if i==4:
#         break
#     else:
#         print(i)
# for i in range(1,5):
#     if i==6:
#         continue
#     else:
#         print(i,end=" ")
# list=[1,2,3,4,5]
# for i in list:
#     print(i,end=" ")
# mycart=[100,200,300,600,800,400,500]
# for i in mycart:
#     if i>600:
#         print("This item is too expensive for you")
#         continue
#         priprint(i,end=" ")

# write pgm calculate sum of all the element in a list using for loop
# list=[1,2,3,4,5,35,20] 
# sum=0
# for X in list:
#     sum=sum+X
# print(sum) 
 
# name="prashant"
# for i in name:
#     print(i,end=" ")
 
#  write a pgm to remove all the duplicate element from a list
# name="prakash"
# for i in name:
#     if name.count(i)>1:
#         name=name.replace(i,"")
# print(name) # This will remove all the duplicate characters from the string "prakash" and print "prk". The count() method is used to count the occurrences of each character in the string, and if a character occurs more than once, it is removed using the replace() method.
 
name="prashant"
# newname=""
# for i in name:
#     if i not in newname:
#         newname=newname+i
# print(newname) # This will also remove all the duplicate characters from the string "prashant" and print "prashnt". The newname variable is used to build a new string that only includes unique characters from the original name string.

# reverese a string using for loop
# newname=""
# for i in name:
#     newname=i+newname
# print(newname) # This will reverse the string "prashant" and print "tn
 
# for i in name:
#     newname=name[::-1]
#     print(newname) # This will also reverse the string "prashant" and print "tnahsarp". The slicing syntax [::-1] is used to reverse the string.

# rollno=[3,2,5,4,53,1]
# for i in rollno:
#     if i==3 or i==5 :
#         print("Even number is found",i)
#     else:
#         print("Even number is not found",i)
#         break #This will check each element in the rollno list, and if it finds an even number (2 or 4), it will print a message and break out of the loop. If it does not find any even numbers, it will simply finish the loop without printing anything.
    
# s="easy"
# s1=s.replace("difficult","easy")
# print(s1)# This will replace the word "difficult" with "easy" in the string s, and print the resulting string s1. Since s is an empty string, s1 will also be an empty string.
# s="abababababababab"
# s1=s.replace("a", "b")
# print(s1)
# X=['a','b','c','d','e']
# Y=['a','b','c','d','e']
# Z=['f','g','h','i','j']
# print(X==Y)# This will print True because X and Y have the same elements in the same order.
# print(X==Z)# This will print False because X and Z have different elements.
# # it is comaparing address or value of the list
# print(X is Y)

# value=[1,2,3,4,5,1,2,3,4,5,7,6]
# print(value.index(1))

# # This will return the index of the first occurrence of the value 1 in the list, which is 0. The index() method returns the index of the first occurrence of a specified value in the list.
# print(value.count(1))
# print(value.count(2))
# print(value.count(3)) # This will return the count of occurrences of the value 3 in the list, which is 2. The count() method returns the number of times a specified value appears in the list.
# print(value.count(7))
# print(value.count(6)) # This will raise a ValueError because the value 6 is not present in the list. The index() method will only return the index of the first occurrence of a value if it is found in the list, otherwise it will raise an error.

# import datetime
# month=datetime.datetime.now().month
# now=datetime.datetime.now()
# print(month)
# print(now)
# #   i want one month calendar
# import calendar
# year=2024
# month=6
# print(calendar.month(year,month)) # This will print the calendar for the month of June in


# while loop
#  while syntax:
#      initialization
#      while condition:
#         #  statement
#         #  increment/decrement

i=1
# while i<=5:
#     print(i,end=" ")
#     i=i+1

# write pgm sum of natural number from 1 to 10 using while loop
# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     i=i+1
# print("sum:", sum)

# what to print the count of even and odd number from 1 to 10 using while loop
# i=1
# even_count=0
# odd_count=0
# while i<=10:
#     if i%2==0:
#         even_count=even_count+1
#     else:
#         odd_count=odd_count+1
#     i=i+1
#     continue
# print("Even count:", even_count)
# print("Odd count:", odd_count)

# write a pgm to print the multiplication table of a given number using while loop
# i=1
# num=0
# num=int(input("Enter a number: "))
# while i<=10:
#     print(num,"x",i,"=",num*i)
#     i=i+1

# to prin 1245 & 5421 using  for loop

# for i ,j, in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i,"",j)


# factorial of a number using while loop

# num=int(input("Enter a number: "))
# factorial=1
# while num>0:
#     factorial=factorial*num
#     num=num-1
#     print("Factorial:", factorial)

# username=" "
# password=0
# while username!="prashant" or password!=12345:
#     username=input("Enter your username: ")
#     password=int(input("Enter your password: "))

# nested for loop
# for i in range(1,4):
#     for j in range(1,4):
#         for k in range(1,4):
#             if i==j==k:
#                 print(i,"",j,"",k)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()
# to find second largest number in a list

# list=[2,9,7,3,8,9]
# list.sort()
# print(list)
# print("Second largest number is:", list[2]) # This will sort the list in ascending

# list=[2,9,7,3,8,9]
# list.sort(reverse=True)
# print(list)
# print("Second largest number is:", list[1]) # This will sort the list in descending order


# Function In Python 


# def value(a,b):
#     sum=a+b
#     return sum
# result=value(5,10)
# print(result)

# synttax of function
# def function(parameter):
#     statement 1
#     statement 2
    
#     return value()

# def msg(): #calling function
#     print("hello world")
#     print("welcome to my world")
    
# msg()#calling function
# msg()

# def login():
#     username=input("Enter your username: ")
#     password=int(input("Enter your password: "))
#     if username == password:
#         print("Login successful")
#     else:
#         print("Login failed")
        
# login()

# def add():
#     return 2+3

# #print(add())'
# result=add()
# print("result:", result)


# def add():
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add,sub,mul,div
# result = add()
# print("Results:", result[0])

#  how many types of argumntes passed in funvtion
# ans .they are 4 types of arguments passed in function
# 1. Positional arguments
# 2. Keyword arguments
# 3. Default arguments
# 4. Variable-length arguments /variable number of arguments

# 1.positional arguiments
# def name(a,b):
#     return a+b
# result=name(5,10)
# print("result:", result)
 
# def name(a,b):
#     print(a+b)
    
# name(5,9)


# def personalInfo(fname,lname,age):
#     print("First Name:", fname)
#     print("Last Name:", lname)
#     print("Age:", age)

# personalInfo("Kiran","Kumar",25) # This will call the personalInfo function with the arguments "Prashant" and "Kumar", and print the first name and last name accordingly.    

# keyword arguments

# def profile(fname,lname,age):
#     print("First Name:", fname)
#     print("Last Name:", lname)
#     print("Age:", age)


# profile(fname="Kiran", lname="Kumar", age=25)

# default arguments
# def cityname(city="New York"):
#     print("City Name:", city)
# cityname() # This will call the cityname function without providing an argument, so it will use the default value "New York" and print "City Name: New York".
# cityname("bangalore")

# def city(*name):
#     print(name)

# city("parish","India")
# write a pgm to menu drive program using arthematic function
# def addition():
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     print("Addition:", a+b)
# def substraction():
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     print("Subtraction:", a-b)
# def multiplication():
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     print("Multiplication:", a*b)
# def division():
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     print("Division:", a/b)

    
# while True:
#     print("1","Addition")
#     print("2","Subtraction")
#     print("3","Multiplication")
#     print("4","Division")
#     print("5","Exit")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         addition()
#     elif choice==2:
#         substraction()
#     elif choice==3:
#         multiplication()
#     elif choice==4:
#         division()
#     elif choice==5:
#         print("Exiting the program...")
#         break
#     else:
#         print("Invalid choice. Please try again.")
    
    

    
#  to finf calculate  factorial of number

# def fac():
#     num=int(input("Enter a number"))
#     fac=1
#     for i in range(1,num+1):
#         fac=fac*i
#     print(fac)
# fac()   
    

# exceptional handling in python
# run time error is called exceptional handling in python
# snytax errror is called compile time error in python
# try:
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second number: "))
#     result=num1/num2
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid number.")


# def value():
#     try:
#         num1=int(input("Enter first number: "))
#         num2=int(input("Enter second number: "))
#         result=num1+num2
#         print("Addition:", result)
#         result=num1-num2
#         print("Subtraction:", result)
#         result=num1*num2
#         print("Multiplication:", result)
#         result=num1/num2
#         print("Division:", result)
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero.")
#     except ValueError:
#         print("Error: Invalid input. Please enter a valid number.")

# value()


#  predefined functions in python
# user defined functions in python

# try:
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter another number: "))
#     print(num1/num2)
# except ValueError:
#     print("Error: Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")

# try:
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter another number: "))
#     print(num1/num2)
# except (ZeroDivisionError, ValueError, TypeError, NameError) as message:
#     print("Error:", message)

# try:
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter another number: "))
#     print(num1/num2)
# except (ZeroDivisionError, ValueError, TypeError, NameError) as message:
#     print("Error:", message)
# except:
#     print("An unexpected error occurred.")

# try:
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter another number: "))
#     print(num1/num2)
# except (ZeroDivisionError, ValueError, TypeError, NameError) as message:
#     print("Error:", message)
# else:
#     print("An unexpected error occurred.")

# try:
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter another number: "))
#     print(2/4)
# except (ZeroDivisionError, ValueError, TypeError, NameError) as message:
#     print("Error:", message)
# else:
#     print("An unexpected error occurred.")
# finally:   
#     print("This block will always be executed, regardless of whether an exception occurred or not.")

# try:
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter another number: "))
#     try:
#         print(num1/num2)        
#     except ZeroDivisionError as message:
#         print("Error:", message)
# except ValueError as message:
#     print("Error:", message)
    
