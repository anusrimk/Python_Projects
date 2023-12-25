'''
a
nn
uuu
ssss
rrrrr
iiiiii
n=str(input("Enter String :  "))
length  = len(n)
for i in range(0 , length):
    for j in range(0, i + 1):    
            print(n[i], end="")       
    print()'''

'''
E
DE
CDE
BCDE
ABCDE
n=int(input("Enter length: "))
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(chr(j+64),end="")
    print("")'''

'''
A B C D E F G 
 B C D E F G 
  C D E F G 
   D E F G 
    E F G
rows = int(input("Enter the number: "))
for i in range(rows):
    for j in range(i):
        print("", end=" ")
    for k in range(i-2, rows):
        print(chr(65 + k+2), end=" ")
    print()''' 
    
'''
    *        *
   ***      ***
  *****    *****
 *******  *******
******************
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(i, rows):
        print(" ", end="")
    
    for j in range(1, 2 * i):
        print("*", end="")
    
    for j in range(2 * i, 2 * rows):
        print(" ", end="")
    
    for j in range(1, 2 * i):
        print("*", end="")
    
    print()'''
       
'''
      a
     an
    anu
   anus
  anusr
 anusri
 def print_pattern(user_string):
    n = len(user_string)

    for i in range(n):
        # Print spaces
        for j in range(n - i ):
            print(" ", end="")
        
        # Print characters
        for k in range(i + 1):
            print(user_string[k], end="")
        
        print()
user_input = input("Enter a string: ")
print_pattern(user_input)
 '''
#user_string = input("Enter a string: ")

#for i in range(len(user_string)-1, -1, -1):
    #print(user_string[i:], end=" \n")
    
'''user_string = input("Enter a string: ")

for i in range(len(user_string)):
    pattern = user_string[i:] + user_string[:i]
    print(pattern, end=" ")'''
    
'''
  c  d  e

 b  c  d  e 

a  b  c  d  e  

 b  c  d  e 

  c  d  e
  for char5 in range(ord('c'),ord('e')+1):
    print(" ",chr(char5),end="")
print('\n')


for char4 in range(ord('b'),ord('e')+1):
    print("",chr(char4), end=' ')
print('\n')

for char in range(ord('a'),ord('e')+1):
    print(chr(char),end="  ")
print("\n")

for char1 in range(ord('b'),ord('e')+1):
    print("",chr(char1), end=' ')
print('\n')

for char3 in range(ord('c'),ord('e')+1):
    print(" ",chr(char3),end="")
'''