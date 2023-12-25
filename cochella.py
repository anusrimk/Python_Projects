print(" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("                       WELCOME TO COACHELLA VALLEY MUSIC AND ARTS FESTIVAL                        ")
print(" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


#concert_management for coachella music festival
#Artists
print()
print()
print('-----------------------------------------------------------------------------')
print('                          CONCERT DATES                                      ')
print('-----------------------------------------------------------------------------')

from collections import namedtuple

MenuEntry = namedtuple('MenuEntry', ['index','description','price'])
_menu = []
_menu.append(MenuEntry(1, '22 February', 'Tuesday-(6 to 10 pm)'))
_menu.append(MenuEntry(2, '23 February', 'Wednesday-(6 to 10 pm)'))
_menu.append(MenuEntry(3, '24 February', 'Thursday-(6 to 10 pm)'))
_menu.append(MenuEntry(4, '25 February', 'Friday-(6 to 10 pm)'))

for entry in _menu:
   index = str(getattr(entry,'index')).ljust(5)
   descr = getattr(entry,'description').ljust(25)
   price = getattr(entry,'price').ljust(7)
   print ('{0}{1}{2}'.format(index,descr,price))
print()

a='Y'
while (a=='Y'):
   
   print("We have a limited period LOTTERY OFFER!!!! Grab it now!!!!")
   print("1. The Surface Details of the Program")
   print("2. Know About Your Favourite Artist")
 
   opt=int(input("Enter your choice:"))
   print()
   print(" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
   if opt==1:
    
    print( ''' Coachella showcases popular and established musical artists as well as emerging artist and reunited groups.
    It is one of the largest, most famous, and most profitable music festivals in the United States and the world.
    Each Coachella staged from 2013 to 2015 set new records for festival attendance and gross revenues.''')
   print(" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
   if opt==2:
       stop='N'
       new='Y'
       while(new=='Y'):
          
    
          print("A. Tailor Swift")
          print("B. BlackPink")
          print("C. Billie Eiliesh")
          print("D. Harry Styles")
          print("E. Ariana Grande")
    
          ch1=input("Enter your choice(A/B/C/D/E):")
          print(" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
          if (ch1=='A'):
             
             


              print("\n Taylor Allison Swift (born December 13, 1989) is an American singer-songwriter, record"
                          "\n producer,"
                          "\n music video director, philanthropist, and actress. As one of the world's leading contemporary"
                          "\n recording artists, she is known for narrative songs about her personal life, which have received"
                          "\n widespread media coverage. Having sold more than 50 million albums—including 37 million in the US,"
                          "\n Swift is one of the world's best-selling music artists and the highest-earning female musician"
                          "\n of the 2010s. She has won 10 Grammy Awards, an Emmy Award, six Guinness world records and is the"
                          "\n most-awarded act and woman at the American Music Awards (29 wins) and Billboard Music"
                          "\n Awards (23 wins), respectively. She has a fantastic carrier including which some of her famous"
                          "\n songs called 'All Too Well','Shake It Off' and 'Blank Space' make up a wonderful list."
                          "\n YouTube link: https://youtu.be/iM_j8_AZJW ")
              print()
              print(" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
              new=input('Do you want to continue(Y/N)')
              
            
           
          if (ch1=='B'):
             
             print("\n BLACKPINK is a South Korean girl group that debuted on 8 August 2016. The group consists of"
                  "\n members Jisoo, Jennie, Rosé, and Lisa. They are the highest-charting female K-pop act"
                  "\n on both Billboard Hot 100 and Billboard 200. They are also the first and only K-pop girl group"
                  "\n to enter and top the Billboard's Emerging Artists chart. In addition, BLACKPINK are also the"
                  "\n first female K-pop group to have four number-one singles on Billboard's World Digital Song"
                  "\n Sales chart. Their 2018 song 'Ddu-Du Ddu-Du' was the most-viewed Korean music video in the"
                  "\n first 24 hours on YouTube. In January 2019, it became the most viewed music video by a K-pop"
                  "\n group on YouTube. They are currently the most subscribed music act, K-pop group and female"
                  "\n artist on Youtube.[4] BLACKPINK was also the first female K-pop group to perform at Coachella."
                  "\n YouTube link: https://youtu.be/-f0MQzVMuUE ")
             print()
             print(" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
             print()
            
             new=input('Do you want to continue(Y/N)')

          if(ch1=='C'):
             print("\n Billie Eilish is a famous American songwriter and singer. She is best known for her successful"
                  "\n debut single, ‘Ocean Eyes.’ Billie performed the song and released it online. It became a"
                  "\n massive success. This turned out to be her first massive breakthrough.Darkroom released"
                  "\n Eilish’s 'Don’t Smile at Me' in August 2017, an eight-song EP written by Eilish and FINNEAS."
                  "\n The EP wasreissued with a bonus track in December 2017; two more bonus tracks were added in"
                  "\n later reissues. Following its release, 'Don’t Smile at Me' peaked at 14 on the Billboard 200"
                  "\n chart."
                  "\n YouTube link: https://youtu.be/66TYJJObd6E ")
             print()
             print(" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
             print()
                  
             new=input('Do you want to continue(Y/N)')
            

          if (ch1=='D'):
             print("\n Harry Edward Styles (born 1 February 1994) is an English singer, songwriter and actor."
                  "\n His musical career began in 2010 as a solo contestant on the British music competition"
                  "\n series The X Factor. It debuted at number one in the UK and the US, and became one of the"
                  "\n world's top-ten best-selling albums of the year. He has a fantastic carrier which include"
                  "\n some of his famous songs like 'Sign of the Times', 'Golden', and 'Lights Up'."
                  "\n YouTube link: https://youtu.be/zhjBetvgQXA ")
             print()
             print(" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
             print()
             new=input('Do you want to continue(Y/N)')
                 
           

          if (ch1=='E'):
             print("\n[22:29, 08/02/2022] Siri: Grande began singing and acting when she was young. In 2008 she won a role in the"
                  "\n Broadway play 13, and she soon began appearing in bit parts on television shows. Her big"
                  "\n break came in 2010 when she landed a role on the Nickelodeon TV series Victorious. She played"
                  "\n Cat Valentine, a teenager attending a performing arts school. After the sitcom was canceled"
                  "\n in 2013, she starred in the spin-off show Sam & Cat (2013–14). She, as a singer has worked in"
                  "\n famous songs such as 'Seven Rings', 'Thank You, Next', and 'Rain On me'."
                  "\n Youtube link: https://youtu.be/U1gZSpKwv8A ")
             print()
             print(" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
             print()
             new=input('Do you want to continue(Y/N)')

   
   print()
   print('Please confirm again')
   a=input('Do you want to continue(Y/N)')
print()
import random
freeticket=0
print('TRY YOUR LUCK TO WIN 1 FREE 4th row Ticket!!!')
print()
print('''Guess a 4 digit number,
If the number is same as the lottery number,
YOU WILL WIN!!!''')
lottery_number=random.randrange(1000,10000)
print()
user=int(input("Enter any number::"))
if lottery_number==user:
    print("Congratulations you have won 1 lottery ticket of 4th row of the concert")
    freeticket=freeticket+1
    
else:
    print("Sorry you lost the chance :(")
    print('The number was',lottery_number)

print()


#booking for people

student={}

print("Press 1 to Register yourself")
print("Press 2 to update your entries")
print()
op=int(input("Enter your choice:"))
if op==1:
    
    sdetails={}
    rno=int(input("Enter your phone number:"))
    sdetails['Phone number']=rno
    smarks=input("Enter your name:")
    sdetails["Name"]=smarks
    kname=int(input("Enter your age:"))
    sdetails["Age"]=kname
           
    email=input("Enter your email id:")
    sdetails['Email:']=email
    add=input('Enter your address:')
    sdetails['Address']=add
    student[rno]=sdetails
    print(student)
    
opt=int(input('Do you want to update your entry?(If yes, then enter 2)'))
a='Y'
while(a=='Y'):
   if (opt==2):
    
       rno=int(input("Enter phone number:"))
    
        
       print("A.Enter the name you need to update:")
       print("B.Enter the phone number you need to update:")
        
       ch1=input("Enter choice for your updation(A/B/C):")
       if (ch1=="A"):
           nm=input("Enter updated name:")
           student[rno]["Name"]=nm
           print("After updation of name:")
        
    
            
       if (ch1=='B'):
          mk=input("Enter new phone number to update:")
          student[rno]["Phone number"]=mk
   a=input('Do you want to continue with updation?(If yes, enter-Y or else click enter)')
        
if True:
    print()
    print("Details field wise:")
    for  rno,val in student.items():
        print("\nPhone number.:",rno)
        for k in val:
            print(k+":",val[k])

    

    
#date and time

print('-----------------------------------------------------------------------------')
print('                  CONCERT DATES                                      ')
print('-----------------------------------------------------------------------------')

from collections import namedtuple

MenuEntry = namedtuple('MenuEntry', ['index','description','price'])
_menu = []
_menu.append(MenuEntry(1, '22 February', 'Tuesday-(6 to 10 pm)'))
_menu.append(MenuEntry(2, '23 February', 'Wednesday-(6 to 10 pm)'))
_menu.append(MenuEntry(3, '24 February', 'Thursday-(6 to 10 pm)'))
_menu.append(MenuEntry(4, '25 February', 'Friday-(6 to 10 pm)'))






for entry in _menu:
    index = str(getattr(entry,'index')).ljust(5)
    descr = getattr(entry,'description').ljust(25)
    price = getattr(entry,'price').ljust(7)
    print ('{0}{1}{2}'.format(index,descr,price))
print()

print()
date={1:'22 February, Tuesday-6 to 10 pm',2: '23 February, Wednesday-6 to 10 pm',3:'24 February, Thursday-6 to 10 pm',4: '25 February, Friday-6 to 10 pm'}

sel=int(input('Enter the choice you want to add (1,2,3,4):'))
a=date[sel]

student[rno]['Date and time']=a
print()
print(student)


#seating arrangements

print('-----------------------------------------------------------------------------')
print('                  SEATING ARRANGEMENTS                                      ')
print('-----------------------------------------------------------------------------')

from collections import namedtuple

MenuEntry = namedtuple('MenuEntry', ['index','description','price'])
_menu = []
_menu.append(MenuEntry(1, '1st Row + Meet and Greet', 'Rs.18678'))
_menu.append(MenuEntry(2, '1st Row', 'Rs.10490'))
_menu.append(MenuEntry(3, '2nd Row', 'Rs.9800'))
_menu.append(MenuEntry(4, '3rd Row', 'Rs.8700'))
_menu.append(MenuEntry(5, '4th Row', 'Rs.6687'))





for entry in _menu:
    index = str(getattr(entry,'index')).ljust(5)
    descr = getattr(entry,'description').ljust(25)
    price = getattr(entry,'price').ljust(7)
    print ('{0}{1}{2}'.format(index,descr,price))
print()
print("If you don't want to purchase, enter 0")
print()
s1=s2=s3=s4=s5=0
for i in range(1,6):

    sel=int(input('Enter the choice you want to add (1,2,3,4,5):'))
    if sel==0:
        break
    if sel==1:
    
        n1=int(input('Enter the number you want to purchase:'))
        s1=18678*n1
        print("Total amount you are paying:",s1)
    
    if sel==2:
    
        n2=int(input('Enter the number you want to purchase:'))
        s2=10490*n2
        print("Total amount you are paying:",s1+s2)
    if sel==3:
    
        n3=int(input('Enter the number you want to purchase:'))
        s3=9800*n3
        print("Total amount you are paying:",s1+s2+s3)
    if sel==4:
    
        n4=int(input('Enter the number you want to purchase:'))
        s4=8700*n4
        print("Total amount you are paying:",s1+s2+s3+s4)
    if sel==5:
    
        n5=int(input('Enter the number you want to purchase:'))
        s5=6687*n5
        print("Total amount you are paying:",s1+s2+s3+s4+s5)

seatbill=s1+s2+s3+s4+s5
sbill={}
if (s1!=0):
    sbill['1st Row + Meet and Greet']=(n1,s1)
if (s2!=0):
    sbill['1st Row']=(n2,s2)
if (s3!=0):
    sbill['2nd Row']=(n3,s3)
if (s4!=0):
    sbill['3rd Row']=(n4,s4)
if (s5!=0):
    sbill['4th Row']=(n5,s5)
if (freeticket==1):
    sbill['Your free ticket in 4th row']=1
print()
print(sbill)

student[rno]['Your seat details:']=sbill
print()
print(student)

#Food and bevarages
        
print('-----------------------------------------------------------------------------')
print('                  MENU                                       ')
print('-----------------------------------------------------------------------------')

from collections import namedtuple

MenuEntry = namedtuple('MenuEntry', ['index','description','price'])
_menu = []
_menu.append(MenuEntry(1, 'Popcorn', 'Rs.550'))
_menu.append(MenuEntry(2, 'Chips', 'Rs.100'))
_menu.append(MenuEntry(3, 'Kings Burger', 'Rs.760'))
_menu.append(MenuEntry(4, 'Chicken Nuggets', 'Rs.980'))
_menu.append(MenuEntry(5, 'Cheese Fries', 'Rs.590'))
_menu.append(MenuEntry(6, 'Cola', 'Rs.120'))
_menu.append(MenuEntry(7, 'Sprite', 'Rs.180'))



for entry in _menu:
    index = str(getattr(entry,'index')).ljust(5)
    descr = getattr(entry,'description').ljust(25)
    price = getattr(entry,'price').ljust(7)
    print ('{0}{1}{2}'.format(index,descr,price))
print()
print("If yoy don't want to purchase, enter 0")
b1=b2=b3=b4=b5=b6=b7=0
for i in range(1,8):
    sel=int(input('Enter the choice you want to add (1,2,3,4,5,6,7):'))
    if sel==0:
        break

    if sel==1:
    
        n1=int(input('Enter the number you want to purchase:'))
        b1=550*n1
        print("Total amount you are paying:",b1)
    
    if sel==2:
    
        n2=int(input('Enter the number you want to purchase:'))
        b2=100*n2
        print("Total amount you are paying:",b1+b2)
    if sel==3:
    
        n3=int(input('Enter the number you want to purchase:'))
        b3=760*n3
        print("Total amount you are paying:",b1+b2+b3)
    if sel==4:
    
        n4=int(input('Enter the number you want to purchase:'))
        b4=980*n4
        print("Total amount you are paying:",b1+b2+b3+b4)
    if sel==5:
    
        n5=int(input('Enter the number you want to purchase:'))
        b5=590*n5
        print("Total amount you are paying:",b1+b2+b3+b4+b5)

    if sel==6:
    
        n6=int(input('Enter the number you want to purchase:'))
        b6=590*n6
        print("Total amount you are paying:",b1+b2+b3+b4+b5+b6)
    if sel==7:
    
        n7=int(input('Enter the number you want to purchase:'))
        b7=80*n7
        print("Total amount you are paying:",b1+b2+b3+b4+b5+b6+b7)
food=b1+b2+b3+b4+b5+b6+b7


foodbill={}
if (b1!=0):
    foodbill['Popcorn']=(n1,b1)
if (b2!=0):
    foodbill['Chips']=(n2,b2)
if (b3!=0):
    foodbill['Kings Burger']=(n3,b3)
if (b4!=0):
    foodbill['Chicken Nuggets']=(n4,b4)
if (b5!=0):
    foodbill['Cheese fries']=(n5,b5)
if (b6!=0):
    foodbill['Cola']=(n6,b6)
if (b7!=0):
    foodbill['Sprite']=(n7,b7)
print()
print(foodbill)

student[rno]['Your refreshment details:']=foodbill
print(student)

totalbill=food+seatbill
student[rno]['Your total bill']=totalbill

print()
print("Your total bill::", totalbill)
print()
A=int(input("Enter account number:"))
print(A)
import random
yes='y'

while(yes=='y' or yes=='Y'):
    
    otp=random.randrange(1000,10000)
    print('Your One Time Password to enter',otp)
    user=int(input("Enter the one time password::"))
    if otp==user:
       
        print()
        print("Booking confirmed!!!!!")
        break
    else:
        print()
        print("Incorrect OTP")
        yes=input('Resend OTP?(y/Y):')

print()  
print("Details field wise:")
for  rno,val in student.items():
   
   print("\nPhone number.:",rno)
   for k in val:
      
      print(k+":",val[k])
print()
print('THANK YOU!! ENJOY THE SHOW!!!')