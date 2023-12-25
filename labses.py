# a=[1,2,3]
# b=(4,5,6)
# c=()
# length=len(b)
# a.extend(list(b))
# print(a)
# print(length)
# # Python program to create a list of tuples from given list having number and its cube in each tuple

# list1 = [2, 3, 4, 5, 6]
# res = [(val, val**3) for val in list1]
# print(res)

#question 1 16/12/2023
 

print('hello world , How are you ? ')
print("hello world , How are you ?")
print(''''hello world , How are you ?''')
print( """"hello world , How are you ?""")
print(""""hello world ,
 How are you ?""")

#2
# Input string
str_input = "Hello world"

# i. Print complete string
print("i. Complete string:", str_input)

# ii. Print first character
print("ii. First character:", str_input[0])

# iii. Print second character
print("iii. Second character:", str_input[1])

# iv. Print last character
print("iv. Last character:", str_input[-1])

# v. Print second last character
print("v. Second last character:", str_input[-2])

# vi. Print characters from 0th to 4th index
print("vi. Characters from 0th to 4th index:", str_input[0:5])

# vii. Print first 5 characters
print("vii. First 5 characters:", str_input[:5])

# viii. Print characters from 2nd index to 2nd last index
print("viii. Characters from 2nd index to 2nd last index:", str_input[2:-1])

# ix. Print string character by character
print("ix. String character by character:")
for char in str_input:
    print(char)

#3
def find_uncommon_words(str1, str2):
    # Split the strings into words
    words1 = set(str1.split())
    words2 = set(str2.split())

    # Find uncommon words using symmetric difference
    uncommon_words = words1.symmetric_difference(words2)

    return uncommon_words

# Example usage
string1 = "This is a sample sentence."
string2 = "Here is another example sentence."

uncommon_words_result = find_uncommon_words(string1, string2)

print("Uncommon words:", uncommon_words_result)

#4

def is_binary(string):
    # Set of valid binary digits
    valid_digits = {'0', '1'}

    # Check if all characters in the string are valid binary digits
    return all(char in valid_digits for char in string)

# Input string
input_string = input("Enter a string: ")

# Check if the string is binary or not
if is_binary(input_string):
    print("The given string is binary.")
else:
    print("The given string is not binary.")



#5
def least_frequent_char(input_str):

    char_frequency = {}

    for char in input_str:
        char_frequency[char] = char_frequency.get(char, 0) + 1


    least_frequent = min(char_frequency, key=char_frequency.get)

    return least_frequent

if __name__ == "_main_":

    user_input = input("Enter a string: ")


    result = least_frequent_char(user_input)

    print(f"The least frequent character is: {result}")
#6
def remove_ith_char(input_str, i):
    # Check if i is a valid index
    if 0 <= i < len(input_str):
        # Use string slicing to remove the i-th character
        modified_str = input_str[:i] + input_str[i+1:]
        return modified_str
    else:
        print("Invalid index. Please provide a valid index.")

# Example usage:
input_string = "example"
index_to_remove = 2

result = remove_ith_char(input_string, index_to_remove)

if result is not None:
    print(f"Original string: {input_string}")
    print(f"String after removing {index_to_remove}-th character: {result}")
#7
class Employee:
    def __init__(self, employee_id, name, gender, city, salary):
        self.employee_id = employee_id
        self.name = name
        self.gender = gender
        self.city = city
        self.salary = salary

    def display_employee_details(self):
        print(f"Id    : {self.employee_id}")
        print(f"Name  : {self.name}")
        print(f"Gender: {self.gender}")
        print(f"City  : {self.city}")
        print(f"Salary: {self.salary}")


# Creating an instance of the Employee class
employee1 = Employee(employee_id=1, name="pankaj", gender="male", city="delhi", salary=55000)

# Displaying the employee details
employee1.display_employee_details()

