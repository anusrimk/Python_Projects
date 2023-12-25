#learning indentation cases
'''num=3
if (num>0):
    print("Num is greater than 0") #this will only print when the condition is true
    #if the indent is not given, indent block error will be shown ie syntax error
print("Just for testing") #this will always be printed'''

#WAP to see if the number is even or odd
'''a=eval(input("Enter a number: "))
if (a%2==0):
    print("The number is even")
elif(a<0):
    print("Number is less then zero therefore invalid")
elif(a==0):
    print("Number is zero therefore invalid")
else:
    print("The number is odd")'''
    

#to classify marks using elif ladder
a=eval(input("Enter a number: "))
if (a>=70):
    print()
    print("Distinction! ")
elif(a>=60 and a<70):
    print()
    print("First Class! ")
elif(a>=50 and a<60):
    print()
    print("Second Class! ")
else:
    print("Pass Class! ")