# FOR STRING SLICING
# str='ITM Skills University'
# #str="Kharghar"
# del str
# print (str)

# print(str[-21:-18])
# print(str[0:3:2])
# print(str[::-1])
# del str[0] #error ayega

#PROGRAM FOR PRINTING LETTERS ONE-BY-ONE OF A STRING

#WITHOUT USING LENGTH FUNCTION
# str='ITM Skills University'
# for letter in str:
#     print(letter)

#USING LENGTH FUNCITON
# str='ITM Skills University'
# length=len(str)
# for i in range(0,length):
#     print(str[i])

#WHILE LOOP
# str='ITM Skills University'
# i=0
# length=len(str)
# while(i<length):
#     print(str[i])
#     i+=1

#STRING.FIND FUNCTION
# str='ITM Skills University'
# print(str.find('I'))
# print(str.find('ITM'))
# print(str.find('Skills',1))
# print(str.find('Skills',1,18))

#PROGRAM TO FIND UPPERCASE AND EVEN LOWERCASE CHARACTERS

#for skills in string
# str='ITM Skills University'
# if 'ITM' in str: #if not in (agar vo string ke andar nahi hai)
#     print("It is there")
# else:
#     print("It is not")


# #to find cmmmon characters in each string
# string_input1 = input("Enter a string: ")
# string_input2 = input("Enter a string: ")
# for letter in string_input1:
#     if letter in string_input2:
#         print(letter)


#to conmpare thre capital and small ltter intwo strings
# string1=str(input("Enter 1st string: "))
# string2=str(input("Enter 2nd string: "))
# # for char in string1:
# #     if char .isupper in string1:
# #         print("The string is upper! ")
# if string1>string2:
#     print("The string 1 is greater! ")
# elif string2>string1:
#     print("The string 2 is greater! ")
    
    
#ESCAPE SEQUENCEẼ

# print("Hey! What's up")
# print("Hey! \"What's up\"") #the \ makes the interpreter ignore the character after the slash so the 
# #apostrophie is ignored varna error dikhata that since it is not closed properly
# print('Hey! Whats\ up')
# print(r'Hey! "Whats up"') # r means raw string and yeh bas single quotes me kaam karna chahiye
# # print("Hey!\n\"Whats up"")
# print("Hey,\t\"Whats up\"")

#f string is format string placeholder curly braces hota hai
print("Welcome to{},{}".format("ITM","Kharghar"))
print("Welcome to{1},{0}".format("Kharghar","ITM"))
print("Welcome to{b},{a}".format(a="Kharghar",b="ITM"))

