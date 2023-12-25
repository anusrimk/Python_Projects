#max od 3 numbers
def find_max_of_three(num1, num2, num3):
    return max(num1, num2, num3)

result = find_max_of_three(10, 5, 8)
print("The maximum of the three numbers is:", result)

#sum of 3 in list
def sum_of_list(numbers):   
    return sum(numbers)
my_list = [1, 2, 3, 4, 5]
result = sum_of_list(my_list)
print("The sum of the numbers in the list is:", result)

#multipication of numbers in a list
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

my_list = [1, 2, 3, 4, 5]
result = multiply_list(my_list)
print("The product of the numbers in the list is:", result)

#reverse a string
def reverse_string(input_string):
    return input_string[::-1]

original_string = "12345abcd"
reversed_string = reverse_string(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)

#factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is:", result)

#square and cube
def square(number):
    return number ** 2

def cube(number):
    return number ** 3

my_number = 4
square_result = square(my_number)
cube_result = cube(my_number)

print(f"The square of {my_number} is:", square_result)
print(f"The cube of {my_number} is:", cube_result)

#list and produced new list
def unique_elements(input_list):
    return list(set(input_list))

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = unique_elements(sample_list)

print("Sample list:", sample_list)
print("Unique list:", unique_list)

#counts upper and lower meeting
def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

test_string = "Today is my best day"
result = count_upper_lower(test_string)

print("Original string:", test_string)
print("Number of uppercase letters:", result[0])
print("Number of lowercase letters:", result[1])

#plaindrom or not
# function to check string is
# palindrome or not
def isPalindrome(str):

	# Run loop from 0 to len/2
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True

s = "malayalam"
ans = isPalindrome(s)

if (ans):
	print("Yes")
else:
	print("No")

#perfect number or not
num=int(input("Enter the number: "))  
sum_v=0  
for i in range(1,num):  
    if (num%i==0):  
        sum_v=sum_v+i  
if(sum_v==num):  
    print("The entered number is a perfect number")  
else:  
    print("The entered number is not a perfect number")   
    
#self.total_balance= self.amount_to_deposit+self.prev_balance
#self.total_balance= self.prev_balance-self.amount_to_withdraw
# print("Name: ",self.name)
# print("Account Number: ",self.acc_no)
#self.name=input("Enter name: ")
#self.acc_no=int(input("Enter Account number: "))