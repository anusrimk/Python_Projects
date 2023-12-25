# prggram to find the first occurance of s character in a string
# stringfind=str(input("Enter a string: "))
# n= list(stringfind)
# l=[]
# #n = int(input("Enter the number of elements you want to enter: "))


# def findchar():
#     for i in n:
#         x = int(input(f"Enter the number {i + 1}: "))
#         l.append(x)
#         length=len(l)
 
#     find = int(input("Enter the number you want to check: "))
#     #count = l.count(find)
#     for i in range(n):
#         if l[i]==find:
#             countnum=l.count(find)
#             #count+=1
#             print(f"Index of {find} :",i+1)
#     print(f"The number {find} occurs {countnum} times in the list.")
    
# findchar()


def find_char_occurrence():
    string_input = input("Enter a string: ")
    char_to_find = input("Enter the character you want to find: ")

    indices = []

    for i, char in enumerate(string_input):
        if char == char_to_find:
            indices.append(i)

    if indices:
        print(f"The character '{char_to_find}' is found at indices: {', '.join(map(str, indices))}.")
        print("The character ",char_to_find," occurs ",len(indices)," times in the string.")
    else:
        print(f"The character '{char_to_find}' is not found in the string.")

find_char_occurrence()