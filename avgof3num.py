'''a=int(input("Enter first number:"))
b=int(input("Enter first number:"))
c=int(input("Enter first number:"))

def avgof3num():
    s=a+b+c
    x=s/3
    print("Average of 3 numbers is: ", x)
    
avgof3num()'''


def avgof3num():
    z=int(input("How many values do you need to enter: "))
    for i in range(0,z):
        a=int(input("Enter ",i+1,"th number: "))
        i+1
        a=+i
        x=a/z
        print("Average of ",z," numbers is: ", x)
    
avgof3num()
 #cin >> arr[i];
  