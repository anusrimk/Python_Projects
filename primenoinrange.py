#to check prime numbers in a given rannge
lowerlimit=int(input("Enter lower limit: "))
upperlimit=int(input("Enter upper limit: "))
i=2
j=1
for i in range(lowerlimit,upperlimit+1):
    for j in range(2,j<=i):
        if i%j==0:
            continue
        else:
           print(i)