#WAP to calculate area of square by simple class single inheritance
# class Shape:
#     def dimension_area_calc(self,x,y):
#         return x*y
# class Square(Shape):
#     def area_square(self):
#         x = int(input("Enter length: "))
#         y = int(input("Enter breath: "))
#         area_sq=self.dimension_area_calc(x,y)
#         print("The area is: ",area_sq)
# sq=Square()
# sq.area_square()



# class Shape:
#     def add(self,x,y):
#         return self.x + self.y
# class Square(Shape):
#     def take_area(self):
#         self.x=int(input("Enter Length: "))
#         self.y=int(input("Enter Breath: "))
#         result = self.add(self.x,self.y)
#         print(result)
# sq=Square()
# sq.take_area()



# class Shape:
#     def dimension(self,length=None,breath=None,side_length=None ):
#         if length!=None and breath!=None:
#             def rect_area(self,length,breath):
#                 return length*breath
#         else:
#             def sq_area():
#                 return side_length*side_length
# class Area(Shape):
 



#WITHOUT USING ARGS
# class asking():
#     def square(self, a):
#         return a ** 2

#     def rectangle(self, x, y):
#         return x * y

# class cal(asking):
#     def area(self):
#         self.a = int(input("Enter the side: "))
#         result = self.square(self.a)
#         print(result)

#     def areas(self):
#         self.x = int(input("Enter length : "))
#         self.y = int(input("Enter the breath : "))
#         result = self.rectangle(self.x, self.y)
#         print(result)

# choice = int(input("Enter your choice which calculation you want to perform 1.square / 2. rectangle : "))
# if choice == 1:
#     obj = cal()
#     obj.area()
# elif choice == 2:
#     obj = cal() 
#     obj.areas()
# else:
#     print("some error occurred!")

    

class Shape:
    def area(self, x, y = None):
        if y is None:
            return x * x
        else:
            return x * y

class Area(Shape):
    def take_values(self):
        self.option = int(input("Enter 1 for square or 2 for rectangle: "))
        if self.option == 1:
            self.x = float(input("Enter the length of side for area of square: "))
        elif self.option == 2:
            self.x = float(input("Enter the length for area of rectangle: "))
            self.y = float(input("Enter the breadth for area of rectangle: "))
        else:
            print("Invalid Option")

obj = Area()
obj.take_values()

if obj.option == 1:
    print("Area of the square is: ", obj.area(obj.x))
elif obj.option == 2:
    print("Area of the rectangle is: ", obj.area(obj.x, obj.y))