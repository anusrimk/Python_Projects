#program to print just numbers upto a preferred count
'''num=eval(input("Enter a value to print upto:"))
sum=0
for i in range(0,num+1):
    sum=+i
    print(sum)'''

#to print the sum upto a given number
'''num=eval(input("Enter a value to print upto:"))
sum=0
for i in range(num+1):
    sum+=i
print("Sum of", num,"digits is: ", sum)'''

#to print the list of sum after every addition
'''num=eval(input("Enter a value to print upto:"))
sum=0
for i in range(num+1):
    sum+=i
    print("Sum of", num,"digits is: ", sum+i)'''
    
    
#star pattern
''' 
*
**
***
****
*****'''
'''n = int(input("Enter the number of rows: "))       
for i in range(0, n):    
        for j in range(0, i + 1):    
            print("* ", end="")       
        print() '''  

#utla pyramid
# right triangle star pattern
''' 
    *
   **
  ***
 ****
*****'''
'''size=int(input("Enter rows: "))
for i in range(size):
    for j in range(1, size - i):
        print(" ", end="")
    for k in range(0, i + 1):
        print("*", end="")
    print()'''
    
    
#star pattern inverted
''' 
*****
****
***
**
*  '''
'''n = int(input("Enter the number of rows: "))       
for i in range(n+1,0,-1):
    for j in range(0, i-1):    
            print("* ", end="")   
    print("") '''


#star pattern inverted
''' 
*****
 ****
  ***
   **
    *  '''
# downward triangle star pattern
'''size=int(input("Enter rows: "))
for i in range(size):
    for j in range(i):
        print(" ", end="")
    for j in range(size, i, -1):
        print("*", end="")
    print()'''
    
    
#to print a pyramid    
# pyramid star pattern
''' 
    *
   ***
  *****
 *******
*********  '''
    
'''n =int(input("Enter rows: "))
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()  '''

# reverse pyramid pattern
'''
*********
 *******
  *****
   ***
    *'''
'''n =int(input("Enter rows: "))
for i in range(1, n+1):
    # printing spaces
    for j in range(i-1):
        print(' ', end='')
    # printing stars
    for j in range(2*(n-i)+1):
        print('*', end='')
    print()'''

#diamond shape
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *'''
    
#upper triangle
'''n =int(input("Enter rows: "))
for i in range(n):
    for j in range(n - i-1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()
#bottom triangle
for i in range(n-1):
    # printing spaces
    for j in range(i+1):
        print(' ', end='')
    # printing stars
    for j in range(2*(n-i-1)-1):
        print('*', end='')
    print()'''

#hollow pattern
# hollow square pattern
'''
*****
*   *
*   *
*   *
*****'''
'''size =int(input("Enter rows: "))
for i in range(size):
    for j in range(size):
        # print * completely in first and last row
        # print * only in first and last position in other rows
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()'''
#box pattern
# Square pattern program
'''
*****
*****
*****
*****
***** '''
'''size=int(input("Enter number of rows: "))
for i in range(0, size):
    # Create a list of columns
    for j in range(0, size):
        print("*", end="")
    print()'''

#printing alphabets
'''
0
11
222
3333
44444'''
#n=str(input("Enter string: "))
'''l=int(input("Enter number of rows: "))
for i in range(l+1):
    for j in range(0, i + 1):    
            print(i, end="")       
    print()'''

'''
A
BB
CCC
DDDD
EEEEE'''
'''
n=str(input("Enter String :  "))
length  = len(n)
for i in range(0 , length):
    for j in range(0, i + 1):    
            print(n[i], end="")       
    print()
'''

# hollow diamond star pattern
'''
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *'''
    

row = int(input('Enter number of row: '))

# Upper part of hollow diamond
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part of hollow diamond
for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
    
#weird pattern
'''n=int(input("Enter value: "))
# upward hollow pyramid
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# downward pyramid
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        if j == 0 or j == 2*(n - i - 1) - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()'''
# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
        
# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
