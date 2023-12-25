#to sort list based on length
num=eval(input("Enter the elements you want: "))
lst=[]
for i in range (num):
    liist=input("Enter list elements: ")
    lst.append(liist)
def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2
print(Sorting(lst))