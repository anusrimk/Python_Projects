# def function_name(name,age):
#    print(name,age)
# function_name(name="ABC",age=32)
# function_name("ABC",32)
# function_name("ABC",age=32)
#function_name(age=32,"ABC",) #will show error ese because you cant change the order of the positional arguement
#function_name(name="ABC",32) #positional  arguement cannot appear after positional argument


#*args can be written an *anusri ie any name can be given


#ARGS AND KWARGS
#* for keyord based and ** (2 times) for arbitrary based arguements
#def func_name(**anusri):

#STACK DIAGRAM

# def main():
#    a=10
#    b=55
#    #print("In function main....dir()=%s" % (dir()))
#    print("In function main...dir()=",dir())
#    result=absdiff(a,b)
#    #print("The absolute value of %d -%d=%d"  %(a,b,result))
#    print("The absolute value of ",a,"-",b,"=", result)
   
# def absdiff(x,y):
#    print("In function absdiff....dir()=", dir())
#    if x>y:
#       z=x-y
#    else:
#       z=y-x
#    return z
# main()

#DISTANCE BETWEEN TWO POINTS #INCREMENTAL DEVELOPMENT

# def dist(x1,x2,y1,y2):
#    d_x=x2-x1
#    d_y=y2-y1
   
#    sq_x=d_x*2
   
#SAME FOR POINT IN A CIRCLE

import math

def dist ( x1,y1,x2,y2):
    dist_x1 = abs(x1-x2)
    dist_x2 = abs(y1-y2)

    distance = math.sqrt((dist_x1*dist_x1) + (dist_x2*dist_x2))
    print("IN DIST : ",dir())
    return distance


def cirumference(x1,y1,x2,y2):
   
    r = dist(x1,y1,x2,y2) 
    print("IN CIRCUM : ",dir())
    return (2*(22/7)*r)


print(f"{cirumference(1,4,2,6):0,.2f}")