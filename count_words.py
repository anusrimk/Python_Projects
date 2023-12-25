#tp print the number of words in a string

string1 = input("Enter string: ")
word_list = string1.split()
word_count = len(word_list)

print("Number of words in the string:", word_count)
