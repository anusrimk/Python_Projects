#while loop first progam on 2nd dec
'''num=int(input("Enter a number: "))
sum=0
i=1
while(i<=num):
    sum+=i
    i+=1
print("The sum of numbers is: ", sum)'''

#LCM of any two user entered number
import math
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
i=1
lcm=0
def lcm(num1, num2):
    gcd = math.gcd(num1, num2)
    lcm = (num1 * num2) //gcd
    print("Through function: ",lcm)
lcm(num1,num2)

while i<=num1 and i<=num2:
    if num1%i==0 and num2%i==0:
        lcm=i
    i+=1
lcmm=(num1*num2)//lcm
print("This lcm is through while loop: ", lcmm)
        