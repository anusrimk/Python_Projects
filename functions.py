# #function hello world using only print
# def helowrld():
#     print("Hello World")
# helowrld()

# #function hello world using return
# def rethelowrld():
#     return ("Hello World")
# str1=rethelowrld()
# print(str1)

# #function hello world without assigning function call to variable
# def retprhelowrld():
#     return print("Hello World")
# retprhelowrld()

# #function to add
# def add(a,b): #formal parameter
#     sum=a+b
#     print("The sum is: ",sum)
# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# add(a,b) #actual parameter


#args and kwargs
# def my_func(*args):
#     num=int(input("Number of arguements you want to enter: "))
#     for i in range(1,num+1):
#         numbers=eval(input("Enter number: "))
#         i+=1
#         numbers=args
#         for j in args:
#             sum=args[j]+args[j+1]
#             print(j)
# my_func()

#to take in element for a list from the users and use args function to make the sum of all thw elementd
# def add(*args):
#     sum1=sum(args)
#     print(sum1) 

# l=int(input("Enter number of arguements: "))
# my_list=[]
# for i in range(l):
#     my_list.append(int(input(f"Enter value: ")))

# print(add(*my_list))   

#POSITIONAL ARGUEMENTS
#tuple is formed

#args positional arguement
# def my_fun(a,*args):
#     print(a)
#     print(args)
# my_fun(1,2,3,4,5)

# def my_fun(a,b,*args):
#     print(a)
#     print(b)
#     print(args)
# my_fun(1,2,3,4,5)

#KEYWORD BASED ARGUEMENTS
#dictionary is made
# def kbfunction(**kwargs):
#     print(kwargs)
# kbfunction(name='ABC', age=32)


#unpack this dictionary

# def kbfunction(*args,**kwargs):
#     for key, value in kwargs.items():
       
#         print(args,f'{key}: {value}')
# my_dict = {'name': 'ABC', 'age': 32}
# # Unpacking the dictionary using double-asterisk (**)
# kbfunction('Hello', 'World',**my_dict)

#using both args and kwargs and printitng everything differently

# def kbfunc(*args, **kwargs):
#     print(args)
#     print(kwargs)
    
# kbfunc('Hello', 'World',name='ABC',age=32)

# print welcome <input_name >through ITM THROUGH ARGS

# def welcome_message(**kwargs):
#     name = kwargs.get('name')#, 'Guest')  # Default to 'Guest' if 'name' is not provided
#     print(f"Welcome {name} to ITM")

# # Take input from the user or any other source
# input_name = input("Enter a name: ")

# # Call the function with the provided input_name using kwargs
# welcome_message(name=input_name)

#WITHOUT CHOOSING BETWEE NAME AND AGE

# #Welcome to itm but also ask name and age
# import random
# def welcome_message(**kwargs):
#     name = kwargs.get('name')#, 'Guest')
#     age = kwargs.get('age')#, 'N/A')
#     email = kwargs.get('email')#, 'N/A')
#     roll_no = kwargs.get('roll_no')#, 'N/A')

#     print(f"Welcome {name} to ITM")
#     print(f"Age: {age}")
#     print(f"Email: {email}")
#     print(f"Roll Number: {roll_no}")

# # Take input from the user
# input_name = input("Enter a name: ")
# input_age = input("Enter age: ")
# input_email = input("Enter email: ")
# input_roll_no = (random.randint(100,1000))#("Enter roll number: ",

# # Call the function with the provided information using kwargs
# welcome_message(name=input_name, age=input_age, email=input_email, roll_no=input_roll_no)

#CHOOSING BETWEEN NAME AND AGE
# import random
# checker='Y'

# while checker=='Y':
#     def welcome_message(**kwargs):
#         name = kwargs.get('name', 'Guest')
#         age = kwargs.get('age', 'N/A')
#         email = kwargs.get('email', 'N/A')
#         roll_no = kwargs.get('roll_no', 'N/A')

#         print(f"Welcome {name} to ITM")
#         print(f"Age: {age}")
#         print(f"Email: {email}")
#         print(f"Roll Number: {roll_no}")

#     user_choice = input("Enter '1' to input name, '2' to input age: ")

#     if user_choice == '1':
#         input_name = input("Enter a name: ")
#         input_age = None #'N/A'  # Default age to 'N/A'
#     elif user_choice == '2':
#         input_name = None #'Guest'  # Default name to 'Guest'
#         input_age = input("Enter age: ")
#     else:
#         print("Invalid choice. Please enter '1' or '2'.")
#         exit()

#     input_email = input("Enter email: ")
#     while True:
#         prev_rollno=[]
#         input_roll_no = list(random.randint(100, 1000))
#         #prev_rollno.append(input_roll_no)
#         if input_roll_no not in  prev_rollno:
#             prev_rollno.add(input_roll_no)
#             break
        
#     checker=str(input("Do you want to conitnue:(y/n) ")).upper()
#     # if checker=='Y':
#     #     for i in input_roll_no:
#     #         if input_roll_no in prev_rollno:
#     #             input_roll_no[i]-input_roll_no
#     # else:
#     #     break

# # Call the function with the provided information using kwargs
# print()
# welcome_message(name=input_name, age=input_age, email=input_email, roll_no=input_roll_no)
# print()

# WORKING CODE

import random

def welcome_message(**kwargs):
    name = kwargs.get('name', 'Guest')
    age = kwargs.get('age', 'N/A')
    email = kwargs.get('email', 'N/A')
    roll_no = kwargs.get('roll_no', 'N/A')

    print(f"Welcome {name} to ITM")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Roll Number: {roll_no}")

user_choice = input("Enter '1' to input name, '2' to input age: ")

if user_choice == '1':
    input_name = input("Enter a name: ")
    input_age = 'N/A' 
elif user_choice == '2':
    input_name = 'Guest'  
    input_age = input("Enter age: ")
else:
    print("Invalid choice. Please enter '1' or '2'.")
    exit()

input_email = input("Enter email: ")

existing_roll_numbers = set()  # Keep track of generated roll numbers
while True:
    input_roll_no = random.randint(100, 1000)
    if input_roll_no not in existing_roll_numbers:
        existing_roll_numbers.add(input_roll_no)
        break

print()
welcome_message(name=input_name, age=input_age, email=input_email, roll_no=input_roll_no)
print()