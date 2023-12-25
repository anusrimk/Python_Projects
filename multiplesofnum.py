m=int(input("Enter 1st number: "))
n=int(input("Enter 2nd number: "))
def printMultiples(n, m):
#'takes n and m as integers and finds all first m multiples of n'
    for m in (n,m):
        if n % 2 == 0:
            while n < 0:
                print(n)