# class AtharvPatil:
#     def _init_(self, grandfather_assets):
#         self.grandfather_assets = grandfather_assets

#     def display_grandfather_assets(self):
#         print(f"Grandfather's Assets: ${self.grandfather_assets}")


# class Jadhav(AtharvPatil):
#     def _init_(self, grandfather_assets, father_assets, father_income):
#         super()._init_(grandfather_assets)
#         self.father_assets = father_assets
#         self.father_income = father_income

#     def calculate_total_assets(self):
#         total_assets = self.grandfather_assets + self.father_assets + self.father_income
#         return total_assets

#     def display_father_assets(self):
#         print(f"Father's Assets: ${self.calculate_total_assets()}")
#         print(f"Father's Income: ${self.father_income}")


# class Piyush(Jadhav):
#     def _init_(self, grandfather_assets, father_assets, father_income, son_assets):
#         super()._init_(grandfather_assets, father_assets, father_income)
#         self.son_assets = son_assets

#     def display_total_assets(self):
#         total_assets = self.calculate_total_assets() + self.son_assets
#         print(f"Son's Total Assets: ${total_assets}")
#         print(f"Son's Assets: ${self.son_assets}")


# # Example usage
# grandfather_assets = int(input("Enter Grandfather's asset: "))
# father_assets = grandfather_assets
# father_income =int(input("Enter Father's Income: "))
# son_assets = grandfather_assets + father_assets#int(input("Enter Son's asset: "))



# grandfather = AtharvPatil(grandfather_assets)
# father = Jadhav(grandfather_assets, father_assets, father_income)
# son = Piyush(grandfather_assets, father_assets, father_income, son_assets)

# grandfather.display_grandfather_assets()
# print("\n")
# father.display_father_assets()
# print("\n")
# son.display_total_assets()


#meri creativity


# class Grandfather:
#     def __init__(self, grandfather_assets):
#         self.grandfather_assets = grandfather_assets

#     def display_grandfather_assets(self):
#         grandfather_name="Atharv Patil"
#         print(f"Grandfather's Assets: Rs{self.grandfather_assets}")


# class Father(Grandfather):
#     def __init__(self, grandfather_assets, father_assets, father_income):
#         super().__init__(grandfather_assets)
#         self.father_assets = father_assets
#         self.father_income = father_income

#     def calculate_total_assets(self):
#         total_assets = self.father_assets + self.father_income
#         total_asset=total_assets
       
#     def calculate_son_total_assets(self):
        
#         son_total=self.father_assets+ self.father_income
        
#         son_asset=son_total
        
#     def display_father_assets(self):
#         father_name=input("Enter Father's name: ")
#         print(f"Father's Income: Rs{self.father_income}")
#         print(f"Father's TOTAL Assets: Rs{self.calculate_total_assets()}")


# class Son(Father):
#     def __init__(self, grandfather_assets, father_assets, father_income, son_assets):
#         super().__init__(grandfather_assets, father_assets, father_income)
#         self.son_assets = son_assets

#     def display_total_assets(self):
#         son_name=input("Enter Son's name: ")
#         total_assets = self.calculate_son_total_assets() + self.son_assets
#         print(f"Son's Total Assets: Rs{total_assets}")
#         #print(f"Son's Assets: Rs{self.son_assets}")


# # Example usage
# grandfather_assets = 100000
# father_assets = grandfather_assets#int(input("Enter Father's assets: "))
# father_income = int(input("Enter Father's Income: "))
# son_assets = father_assets+father_income

# grandfather = Grandfather(grandfather_assets)
# father = Father(grandfather_assets, father_assets, father_income)
# son = Son(grandfather_assets, father_assets, father_income, son_assets)

# #print(f"Hi, {Son.son_name},{Father.father_name},{Grandfather.grandfather_name}\n your total asset is: ")
# grandfather.display_grandfather_assets()
# print("\n")
# father.display_father_assets()
# print("\n")
# son.display_total_assets()


class Wife:
    def __init__(self, wife_assets):
        self.wife_assets = wife_assets

    def display_wife_assets(self):
        return self.wife_assets


class Grandfather:
    def __init__(self, grandfather_assets):
        self.grandfather_assets = grandfather_assets

    def display_grandfather_assets(self):
        return self.grandfather_assets


class Father(Grandfather):
    def __init__(self, grandfather_assets, father_assets, father_income):
        super().__init__(grandfather_assets)
        self.father_assets = father_assets
        self.father_income = father_income
    def calculate_total_inherited_assets(self):
        total_inherited_assets = super().display_grandfather_assets()
        return total_inherited_assets

    def calculate_total_money(self):
        total_money = self.father_assets + self.father_income
        return total_money

    def display_father_assets(self):
        total_father_assets = self.calculate_total_money() + super().display_grandfather_assets()
        return total_father_assets


class Son(Father, Wife):
    def __init__(self, grandfather_assets, father_assets, father_income, son_assets, wife_assets):
        Father.__init__(self, grandfather_assets, father_assets, father_income)
        Wife.__init__(self, wife_assets)
        self.son_assets = son_assets

    def calculate_total_assets(self):
        total_assets = (
            super().calculate_total_inherited_assets()
            + super().calculate_total_money()
            + super().display_wife_assets()
            + self.son_assets
        )
        return total_assets

    def display_total_assets(self):
        print("Details:")
        print(f"Grandfather's Assets: Rs{super().display_grandfather_assets()}")
        print(f"Father's Income: Rs{super().calculate_total_money()}")
        print(f"Father's Inherited Assets: Rs{super().calculate_total_inherited_assets()}")
        print(f"Father's Total Assets: Rs{super().display_father_assets()}")
        print(f"Wife's Total Assets: Rs{super().display_wife_assets()}")
        print(f"Son's Total Assets: Rs{self.calculate_total_assets()}")


# Example usage
grandfather_assets = 100000
father_assets = 50000
father_income = 20000
son_assets = 10000
wife_assets = 30000

son = Son(grandfather_assets, father_assets, father_income, son_assets, wife_assets)

son.display_total_assets()
