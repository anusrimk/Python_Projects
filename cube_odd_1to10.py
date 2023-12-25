#that makes a dictionary of the cubes of odd numbers from 1 to 10
#wap that creates a dictionary of cubes of odd number in the range 1 to 10 
a=int(input("Enter from where the range should start: "))
b=int(input("Enter upto which the range should end."))
c = {num: num**3 for num in range(a, b+1) if num % 2 != 0}

print(c)
