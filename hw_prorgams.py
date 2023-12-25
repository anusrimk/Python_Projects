'''#to print sum of two numbers
number1=int(input("Enter 1st number: "))
number2=int(input("Enter 2nd number: "))
print("The sum of both the numbers are: ",number1+number2)
print()

#enter radius and get area
rad=int(input("Enter radius of a circle: "))
print("Area of circle with ",rad, "is: ", 3.14* (rad**2))
print()

#enter length and breath and computer area and perimeter
lengthrec=float(input("Enter length of rectangle: "))
breathrec=float(input("Enter breath of rectangle: "))
print("Area and perimeter of rectangle respectively are ",lengthrec*breathrec, "and ",2*(lengthrec+breathrec))
print()

#WAP to calculate simple interest
principle=float(input("Enter principle amount: "))
rate=float(input("Enter rate of interest: "))
time=float(input("Enter time of interest: "))
print("The simple interest calculated for this is: ", (principle*rate*time)/100)
print()

#to find whether the number is even or odd
a=eval(input("Enter a number: "))
if(a==0):
    print("Number is zero therefore neither even nor odd")
elif(a%2==0):
    print("The number is even")
elif(a<0):
    print("Number is less then zero therefore invalid")
else:
    print("The number is odd")
'''
# # Python program to find the largest number among the three input numbers
# try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     num3 = float(input("Enter third number: "))

#     if (num1 >= num2) and (num1 >= num3):
#        largest = num1
#     elif (num2 >= num1) and (num2 >= num3):
#        largest = num2
#     else:
#         largest = num3
#     print("The largest number is", largest)
# except ValueError:
#     print("Invalid input. Please enter a valid floating-point number.")

'''
checker="Y"
while(checker=="Y" or checker=="y"):
    firstinput= float(input("Enter first number: "))
    secondinput= float(input("Enter second number: "))
    print()
    operation=int(input("Chose among operations(1=+)(2=-)(3=*)(4=/)(5=%)(6=//)(7=**): "))
    if(operation==1):
        print(firstinput+secondinput)
    elif(operation==2):
        if(firstinput>secondinput):
            print(firstinput-secondinput)
        else:
            print(secondinput-firstinput)
    elif(operation==3):
        print(firstinput*secondinput)
    elif(operation==4):
        if(firstinput>secondinput):
            print(firstinput/secondinput)
        else:
            print(secondinput/firstinput)
    elif(operation==5):
        if(firstinput>secondinput):
            print(firstinput%secondinput)
        else:
            print(secondinput%firstinput)
      #print(firstinput%secondinput)
    elif(operation==6):
        if(firstinput>secondinput):
            print(firstinput//secondinput)
        else:
            print(secondinput//firstinput)
      #print(firstinput//secondinput)
    else:
      print(firstinput**secondinput)
    checker=str(input("Do you want to conitnue:(y/n) "))
      
#to check if the given year is leap year or not
year=int(input("Enter the year: "))
if ((year%400==0) and (year%100==0 ))or ((year%4==0) and (year%100!=0)):
    print("The year ", year, " is a leap year!")
else:
    print("The year ", year, " is not a leap year!")

#program o print the table of a given number
number = int(input ("Enter the number of which you want the multiplication table: "))      
rangee=int(input("Enter upto which you want table: "))       
print ("The Multiplication Table of: ", number)    
for count in range(1, rangee+1):   
    print(number, 'x', count, '=', number * count)

#print sum upto a given number
num=eval(input("Enter a value to print upto:"))
sum=0
i=1
for i in range(1,num+1):
    sum+=i
    print("Sum of", i,"digits is: ", sum+i)'''
    
# x=[10,20,30,40,50,60,70,80,90,100]
# print("elements",x[-7:-3])
# y=x
# print(x[2])
# x[1]=12
# z=x.append(101)#x.append(22) #append an element to a list
# z==None
# print(z)
# print(x.sort())#sort
# print(x.pop(4)) #based on last in first out principle LIFO
# print(x.remove(20))
# print(x.remove(7))
# print(x.insert([2],100))
# print(x.count(100))
# s=x+[120,130]
# print(y)
# x=x+[9,10]
# print(x)
# print(y)

#write a program to write two list with even number and odd number
# list = [int(i) for i in input("Enter numbers : ").split()]
# odd = []
# even = []
# for i in list:
#     if(i % 2 == 0):
#         even.append(i)
#     else:
#         odd.append(i)
        
# print("Original List : ",list)
# print("Odd list : ",odd)
# print("Even list : ",even)

#write a program to iterate transverse a list in reverse using rev method and reverse method and slicing and insert
# l1 = []
# n = int(input("enter number of elements required: "))
# for i in range(0, n):
#     element = int(input())
#     l1.append(element)
# print("Original List:", l1)
# # sorting in decending
# for i in range(0, len(l1)):
#   for j in range(i+1, len(l1)):
#     if l1[i] <= l1[j]:
#       l1[i], l1[j] = l1[j], l1[i]
# print("Sorted List", l1)
# print("Reverse order: ",l1[::-1])

#extend by using given approach
# a=[10,20,30,40,50]
# a.extend([60,70,80])
# print(a)
# a.append(90)
# print(a)

#sum and mean of elements of a list

# a=[10,20,30,40,50,60,70,80,90,100]
# sum=0
# length=len(a)
# for i in a:
#     sum+=i
#     i+=1
#     avg=sum/length
# print("Sum: " ,sum)
# print("Average: ",avg)

#to rmemove all duplicates from a list in python
# def Remove(duplicate):
# 	final_list = []
# 	for num in duplicate:
# 		if num not in final_list:
# 			final_list.append(num)
# 	return final_list
	
# # Driver Code
# duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
# print(Remove(duplicate))

#list = [int(i) for i in input("Enter numbers : ").split(",")]

# length = len(list)
# for k in range(0,length):
#     for j in range(k+1,length):
#         if(list[j] == list[k]):
#             list[j] = 0
            
# for i in list:
#     if(i==0):
#         list.remove(i)

# print(list)

# x=[[2,5,4],[1,3,9],[7,6,2]]
# y=[[1,8,5],[7,3,6],[4,0,8]]
# k=[[1,2,3],[2,3,4],[3,4,5]]
# for i in range(len(x)):
#     for j in range(len(x)):
#         k[i][j]=x[i][j]+y[i][j]
# print(k)