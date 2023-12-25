def calculator():
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

calculator()

def squarecube(num):
    checker="Y"
    while(checker=="Y"):
        operation=int(input("Choose between 1=square and 2=Cube: "))
        if operation==1:
            square=num**2
            print("The square of ",num, " is: ",square)
        else:
            cube=num**3
            print("The cube of ",num, " is: ",cube)
        checker=str(input("Do you want to conitnue:(y/n) ")).upper()
num=eval(input("Enter a number: "))
squarecube(num)