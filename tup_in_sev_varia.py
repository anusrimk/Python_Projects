#WAP to unpack a variable in several variables

# fruits=("Strawberry","Mango","Lichi",{"Orange","Po"})
# (a,b,c)=fruits
# print(a)
# print(b)
# print(c)

#TAKE OUT EMPTY TUPLE FROM FROM A LIST removal of empty tuple

'''userdata=[(),(),("",),('a','b'),('a','b','c'),('d')]'''
# user1=[]
# for i in userdata:
#     x=len(tuple[i] in userdata[i])
#     #if None==True in userdata[i]:
#     if x==0:
#         userdata[i].pop(i)
#         i+=1
#     else:
#         user1.append(i)
# print(user1)
'''print("OG List: ",userdata)
userdata=[t for t in userdata if t!=()]
print(userdata)'''

#unzip a list of tuples in individual list
# userdata=[(),(),("",),('a','b'),('a','b','c'),('d')]
# print("OG List: ",userdata)
# for i in userdata:
#     userdata=[t for t in userdata if t!=()]
#     #x=list(tuple(i))
#     x=list(i)
#     print(x)