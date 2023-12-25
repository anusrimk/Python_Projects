# l1 = []
# n = int(input("enter number of elements required: "))
# length=len(l1)
# for i in range(0, n):
#     element = int(input("Enter element: "))
#     l1.append(element)
# print("Original List:", l1)
# num=eval(input("Enter the value you need to find: "))
# for i in l1:
#     i+=1
#     if num in l1:
#         if l1.index(length)==num:
#             print(l1.index)
#             print(num in l1.count())
#     else:
#         print("Not in list")

l = []
indexing=[]
n = int(input("Enter the number of elements you want to enter: "))

for i in range(n):
    x = int(input(f"Enter the number {i + 1}: "))
    l.append(x)
    length=len(l)

find = int(input("Enter the number you want to check: "))
#count = l.count(find)
for i in range(n):
    if l[i]==find:
        countnum=l.count(find)
        #count+=1
        print(f"Index of {find} :",i+1)
print(f"The number {find} occurs {countnum} times in the list.")