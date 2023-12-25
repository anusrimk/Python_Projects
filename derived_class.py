#WAP to show single inheritance
class Parent:
    def add(self, x, y):
        return x + y

class Child(Parent):
    def Total_value(self):
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        result = self.add(x, y)
        print("The sum of", x, "and", y, "is", result)

num = Child()
num.Total_value()