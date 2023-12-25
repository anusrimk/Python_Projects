#butterfly using python
'''import math

def main():
    n = int(input("Enter the size\n"))
    l = math.ceil(2.2 * n)

    for j in range(l, -l-1, -1):
        for i in range(-l, l+1):
            if (pow(abs(i) + 2*j - 2*n, 2) + 5*pow(abs(i) - 2*j, 2) <= 5*pow(n, 2) or
                (pow(abs(i) - j - n, 2) + 2*pow(abs(i) + j, 2) <= pow(n, 2))):
                print("*", end="")
            else:
                print(" ", end="")
        print()

if __name__ == "__main__":
    main()
'''

#5 cornered star using python
n = int(input("Enter a number: "))

for i in range(n):
    for s in range(2*n - i - 1):
        print("  ", end="")
    for j in range(2*i+1):
        if (j == 0 or j == 2*i):
            print("* ", end="")
        else:
            print("  ", end="")
    print()
    
for i in range(n):
    for s in range(i):
        print("  ", end="")

    for j in range(n - i):
        if (j == 0 or i == 0):
            print("* ", end="")
        else:
            print("  ", end="")

    for k in range(2*n - 1):
        print("  ", end="")

    for l in range(n - i):
        if (l == n - i - 1 or i == 0):
            print("* ", end="")
        else:
            print("  ", end="")
    print()

for i in range(n):
    for s in range(n):
        print("  ", end="")
    for j in range(n - i):
        if (j == 0 or j == n - i-1 ):
            print("* ", end="")
        else:
            print("  ", end="")
    for k in range(1, 2*i + 1):
        print("  ", end="")
    for l in range(n - i):
        if (l == 0 or l == n-i-1):
            print("* ", end="")
        else:
            print("  ", end="")
    print()


#asterisk heart using python
'''n = int(input("The number of rows you want star:"))
for i in range(n//2, n, 2):
    
    for j in range(1, n-i ,2):
        print(" ", end="")
    
    for j in range(1, i+1, 1):
        print("*", end="")
    
    for j in range(1, n-i+1, 1):
        print(" ", end="")
   
    for j in range(1, i+1, 1):
        print("*", end="")
    print()


for i in range(n,0,-1):
    for j in range(i, n, 1):
        print(" ", end="")
    for j in range(1, i*2, 1):
        print("*", end="")
    print()'''