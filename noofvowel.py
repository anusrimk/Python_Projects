#WAP to count the number of vowels in a given string

string1 = str(input("Enter a string: "))
string1 = string1.upper()  # Convert the string to uppercase

count = 0

def find_vowel():
    global count
    for char in string1:
        if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            count += 1

    print("The count is:", count)

find_vowel()
