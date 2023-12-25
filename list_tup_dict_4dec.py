
#LISTS BASIC OPERATIONS
'''
x=[1,"hello",(3+2j)]
y=x
print("Entered list is",x)
x.append(12)#the value of lists x and y both will change since they are assigned to each other even if it was y.append
print(y)
x=x+[13,] #here the value of y wont change because a new list space is assigned to it after concatination
print(x)
print(y)
#print(x[2])
#print(x[0:2])'''


#TUPLES BASIC
'''
x=(1,2,3)
print(x[1:])
y=(2,)
print(y)'''


#DICTIONARY EXAMPLES
'''
d={1:"Hello",'two':42,"blah":{1:"yo","dat":"hehe"}}
print(d)
print(d[1])
print(d["blah"][1])
del(d["blah"][1])
del(d[1])
print(d)
'''

#to sort the given list in descending order
'''l1 = []
n = int(input("enter number of elements required: "))
for i in range(0, n):
    element = int(input())
    l1.append(element)
print("Original List:", l1)
# sorting in decending
for i in range(0, len(l1)):
  for j in range(i+1, len(l1)):
    if l1[i] <= l1[j]:
      l1[i], l1[j] = l1[j], l1[i]
print("Sorted List", l1)'''

fruits=["apple","mango","strawberry","banana"]
print(fruits)
#l1 = []
n = eval(input("enter matching element: "))
for i in range(fruits):
    if(n!=fruits):
        print("The element is wrong!")
        continue
    else:
        print("Yay! same element")
        break