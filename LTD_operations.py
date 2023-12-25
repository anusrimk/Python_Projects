#understanding substrings
'''a="012345"
s=a[-2]
print(s)'''


#list modifying content
'''
x=[1,34,'Mumbai']
y=x
print(x[2])
x[1]=12
z=x.append(22) #x.append(22)
z==None
print(z)
print(y)
x=x+[9,10]
print(x)
print(y)
'''
'''it wont show the new added value in the last y because when you add(+) and [] concatenate two lists,
it creates a new list ie new x and since the previosus value of x is assigned to y there it wont 
show the valuses of the new list ie new x'''


#tuple modification
'''x=(1,2,3)
print(x[1:])

y=(1,)
print(y)'''

#dictionary modification
#a={1:"Anusri",2:"Atharva",3: "Patil",4:"Piyush"}
# print(a) # without modification
# print(a[3])
# print(a[1])
# a[2]="Jadhav" #dictionaries add/modify
# a[5]="Pandey"
# a[6]="Romil"
# print (a)
# del(a[6]) 
# print(a)

a={1:"Anusri",2:"Atharva",3: "Patil",4:"Piyush"}
r1={'id':101,'name':'Amit','Age':21}
# r2=r1["id"]
# print(r2)
if a==r1:
    print("True")
else:
    print("False")
    
def generate_square_dictionary(n):
    square_dict = {i: i*i for i in range(1, n+1)}
    return square_dict
n = int(input("Enter the value of n: "))
result_dict = generate_square_dictionary(n)
print(result_dict)

# Initialize an empty dictionary
my_dict = {}

# Adding one element at a time
my_dict[0] = 'Amit'
my_dict[1] = 'Kumar'
my_dict[2] = 23
my_dict[3] = 'Delhi'

# Adding multiple values to a key
my_dict['marks'] = (69, 70, 58)

# Updating an existing Key's Value
my_dict[2] = 25  # Update the value for key 2

# Adding Nested Key value
my_dict[4] = {'Nested': {'Name': 'Shivang', 'Age': 24}}
print(my_dict)

#DIFFERENCE BETWEEN GET AND ACCESS

# r3=r1.getkeys("Amit")
# print(r3)


#copying lists and dictionaries
# l1=[1]
# l2=list(l1)
# l1[0]=22
# print(l1)
# print(l2)

# d1={1:"10"}
# d2=d1.copy()
# d2[1]="Changed"
# print(d1)
# print(d2)