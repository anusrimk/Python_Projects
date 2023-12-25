# mystring =input("Enter a string: ")
# words = mystring.split()
# for char in words:
#     first_char_list = char[0]
#     print(list(first_char_list))

    
# write a program that forms a list of first characters in a list to other list
n=int(input("Enter number of elements: "))
list=[]
list1=[]
for i in range(n):
    a=input("Enter word: ")
    list.append(a)
print(list)
for i in range(n):
    list1.append(list[i][0])
print(list1)

# x = [[2,5,4],[1,3,9],[7,6,2]]
# y = [[1,8,5],[7,3,6],[4,0,9]]
# result=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(x)):
#     for j in range(len(y)):
#         result[i][j]=x[i][j]+y[i][j]
# print(result)