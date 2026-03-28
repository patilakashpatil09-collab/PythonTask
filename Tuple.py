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

import datetime
month=datetime.datetime.now().month
now=datetime.datetime.now()
print(month)
print(now)
#   i want one month calendar
import calendar
year=2024
month=6
print(calendar.month(year,month)) # This will print the calendar for the month of June in
