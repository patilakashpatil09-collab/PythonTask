mylist=["prashant","Ashish","komal","ankush","Ashish",77,"snadip",60,90,"pratik"]
# print(mylist)
# print(mylist[0])
# print(type(mylist))
# print(mylist[0:-1])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[::-1])
# print(mylist[1:8:2])
# print(mylist[2:])
# print(mylist[:5])
# mylist[3]="pratik"
# print(mylist)
# if "prashant" in mylist:
#     print("prashant is in the list")
# else:
#     print("prashant is not in the list")
# mylist.append("kiran")
# mylist.insert(2,"abhijeet")

# print(mylist)
# mylist.remove("Ashish")
# print(mylist)
# newlist=mylist.copy()
# print(newlist)
# print(mylist)
# mylist=[['prashant',77],['Ashish',60],['komal',90],['ankush',80],['Ashish',70],['snadip',85],['pratik',95]]
# print("Example of multidimensional list:")
# print(mylist[1][0])
# print(mylist[1][1])
# print(mylist[2][0])
# print(mylist[2][1])
# print(mylist[3][0])
list1=["prashant","Ashish","komal","ankush","Ashish",77,"snadip",60,90,"pratik"]
# print(list1*4)
list2=[1,8,7,2,5,4,6,3]
# print(list1+list2)
# del list1[2]
# print(list1)
# del mylist[1:3]
# print(mylist)
# list1.clear()
# list2.clear()
# print(list1,list2)
# name=("Akash")
# print(name)
# myname=list(name)
# print(myname)
# list1.reverse()
# print(list1)
# list2.sort()
# print(list2)
# list2.sort()
# list2.sort(reverse=True)
# print(list2)
# list2.sort(reverse=False)
# print(list2)App
mylist=[1,8,7,2,5,4,6,3]
# newlist=mylist
# print(id(mylist))
# print(id(newlist))
# print(newlist)
# for i in range(5):
#     print(i)
# for i in range(1,11):
#     print(2*i,end=" ")
# for i in range (1,11):
#     print("2*i","","3*i","","4*i","","5*i","","6*i","","7*i","","8*i","","9*i","","10*i")
#     print()
# for i in range (1,11):
#     if i%2==0:
#         print("even,= ",i)
#     else:
#         print("odd,= ",i)
# even=0
# odd=0
# for i in range(1,11):
#     if i%2==0:
#         even+=1
#     else:    
#         odd+=1Akas
# print("Even= ",even)
# print("Odd= ",odd)
# username=input("Enter your name: ")
# password=input("Enter your password: ")
# if username=="Akash" and password=="12345":
#     print("Login successful")
# else:
#     print("Login failed")App
# brand=input("Enter the brand name: ")
# if brand=="Apple" or brand=="AppleApp":
#     print("This is an Apple product")
# else:
#     print("This is not an Apple product")
# while True:
#     username=input("Enter your name: ")
#     password=input("Enter your password: ")
#     if username=="Akash" and password=="12345":
#         print("Login successful")
#         break
#     else:
#         print("Login failed, try again")
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
if n1<n2 and n1<n3:
    print("n1 The smallest number is: ")
elif n2<n1 and n2<n3:
    print("n2 The smallest number is: ")
else:
    print("n3 The smallest number is: ")
    