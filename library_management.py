#books=["book1","book2","book3","book4","book5","book6","book7","book8","book9","book10"]
#books= []
'''chose=int(input("Enter your choice: (1=see elements of books\n)(2=add book\n)(3=delete books\n) "))
if(chose==1):
    
'''
choice="Y"
while(choice=="Y" or "y"):
    books={1:"book1",2:"book2",3:"book3"}
    chose=int(input("Enter your choice: (1=see elements of books: )\n(2=add book: )\n(3=delete books: )\n(4=add to your reading list:)\n "))
    if(chose==1):
        print(books)
        
    elif(chose==2):
        key=int(input("Enter serial no: "))
        value=str(input("Enter name of the book: "))
        books[key]=value
        print(books)
    elif(chose==3):
        delchose=int(input("Enter the serial number of the book you want to delete: "))
        del(books[delchose])
        print(books)
    else:
        l1 = []
        
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
        print("Sorted List", l1)
    choice=str(input("Do you want to continue: (Y/y):"))
