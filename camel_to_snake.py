#camel to snake

def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            if snake_case:
                snake_case += '_'
            snake_case += char.lower()
        else:
            snake_case += char
    return snake_case
c = input("Enter a camel case string: ")
snake = camel_to_snake(c)
print("Snake case string: ",snake)