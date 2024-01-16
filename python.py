# # n = int(input("Enter the number of rows:")) 
# # for i in range(1,n+1):
# #     print(i*"*")

# def print_triangle_pattern(height):
#     for i in range(1, height + 1):
#         print('*' * i, end=' \n')

# def print_inverted_triangle_pattern(height):
#     for i in range(height, 0, -1):
#         print('*' * i, end=' \n')

# # Set the height of the triangles
# height = 5

# # Print the patterns in one line
# print_triangle_pattern(height)
# print_inverted_triangle_pattern(height)
'''
    *
   ***
  *****
 *******
*********'''
# n=int(input("Enter a number: "))
# for i in range(1, n+ 1):
#     print(" " * (n - i) "*" * i+(i-1)*"*")
'''
    *
   **
  ***
 ****
*****'''
#ulta samosa
# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     print((n-i)*" "+ ("*"*i))

# input_num=input("Enter a string of numbers: ")
# numbers=input_num.split(" ")
# rev_list=numbers[::-1]
# join_list=" ".join(rev_list)
# print(join_list)

#rhombus

# n=int(input("Enter a number: "))
# for i in range(0,n+1):
#     print((i*" ")+("*"*(n-1 )))

#reverse samosa
# n=int(input("Enter a number: "))
# for i in range(0,n+1):
#     print((i*" ")+(n-i)*"*")

# n = int(input("Enter the Number:"))

# a, b = 1,1
# print(a)
# print(b)
# for i in range(1, n-2):
#     num = a + b
#     print(num)
#     a, b = b, num

# n = 5
# for i in range(1,n+1):
#     print((i *" "),(2(n-i)+1)*" ",i*"*",sep=" ")

n=int(input("Enter a number: "))
for i in range(1,n+1):
    print((i*"*")+((n-i)*" ")+((n-i)*" ")+(i*"*")) 