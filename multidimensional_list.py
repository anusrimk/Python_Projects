my2DList =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(my2DList[0][1])
#LIST CAN HAVE DIFFERENT DATA TYPES AND CAN BE OF DIFFERENT LENGTHS
my2DList =[[1,2,3,'beta'],[5,6.2,7**2,8],[9,10,'e',],[13,14,'billa',16]]
print(my2DList[3][2])
#can have list under a list with oly one element
my2DList =[[['hola','amigos']],[5,6.2,7**2,8],[9,10,'e',],[13,14,'billa',16]]
print(my2DList[0][0][0])
#can have a sublist inside a list
my2DList =[[['hola','amigos']],[5,6.2,7**2,8],[9,10,'e',],[13,14,'billa',[['mickey','donald-duck'],['minnie','goofy']]]]
print(my2DList[3][3][0][1])
#list as a sequence of refence
mylist=['Name',['Month','Date','Year'],'Address',['Home','Cell']]