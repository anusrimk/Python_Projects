# fruits=('apple',"banana",'strawberry','baananananaa')
# # a=fruits.index('banana',0,3)'
# a=fruits.index(1,0,3)
# print(a) 

#WAP THAT SCANS EMAIL ADDRESS AND FORMS A TUPLE OF USER NAME AND DOMAIN
#WAP THAT SCANS EMAIL ADDRESS AND FORMS A TUPLE OF USER NAME AND DOMAIN
d = {"s@gmail.com":("Romil" , "gmail")}


email = "1"

while(not(email == "0")):
    email = input("Enter your email (0 to exit) : ")
    
    if(email in d ):
        print("\n")
        print(email,"Already exists with the values \nNAME : ",d[email][0],"\nDomain : ",d[email][1],"\n\n")
    else:
        domain = email.split("@")
        while(not(domain[1] == "gmail.com" or domain[1] =="Outlook.com" or domain[1] == "isu.ac.in" or domain[1] == "yahoo.com" or domain[1] == "edu.in")):
            print("Enter email with following domains only (gmail.com,Outlook.com,isu.ac.in,yahoo.com,edu.in) : ")
            email = input("\nEnter your email (0 to exit) : ")
            domain = email.split("@")
            

        name = input("Enter the name : ")

        d[email] = (name,domain[1])