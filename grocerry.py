# class Store:
#     def __init__(self):
#         self._products = {
#             'Soap(001)          ': 10.00,
#             'Toothpaste(002)    ': 20.00,
#             'Water Bottle(003)  ': 15.00,
#             'Chimta(004)        ': 25.00,
#         }
#         self._cart = {}
        
#     def display_menu(self):
#         print("Welcome to the Store!")
#         print("Menu:")
#         for code, price in self._products.items():
#             print(f"{code}: Rs{price:.2f}")
        
#     def take_order(self):
#         while True:
#             code = input("Enter the product code (or 'done' to finish): ").upper()
#             if code.lower() == 'DONE':
#                 break

#             if code in self._products:
#                 quantity = int(input(f"How many units of {code} do you want? "))
#                 if code in self._cart:
#                     self._cart[code] += quantity
#                 else:
#                     self._cart[code] = quantity
#             else:
#                 print("Invalid product code! Please try again!!.")
                
#     def generate_bill(self):
#         print("\n\n===== Your Bill =====")
#         total_amount = 0.0
#         for code, quantity in self._cart.items():
#             price = self._products[code]
#             subtotal = price * quantity
#             total_amount += subtotal
#             print(f"{code}: Rs{price:.2f} x {quantity} = Rs{subtotal:.2f}")

#         print("=====================")
#         print(f"Total Amount: Rs{total_amount:.2f}")

# # # Print product names and prices
# # print("Soap:            10.00")
# # print("Toothpaste:      20.00")
# # print("Water Bottle:    15.00")
# # print("Chimta:          25.00")

# if __name__ == "__main__":
#     my_store = Store()
#     my_store.display_menu()
#     my_store.take_order()
#     my_store.generate_bill()






# import random

# class Store:
#     def __init__(self):
#         self._products = {
#             'Soap': 10.00,
#             'Toothpaste': 20.00,
#             'Water Bottle': 15.00,
#             'Chimta': 25.00,
#         }
#         self._cart = {}

#     def display_menu(self):
#         print("Welcome to the Store!")
#         print("Menu:")
#         for code, price in self._products.items():
#             print(f"{code}: Rs{price:.2f}")

#     def take_order(self):
#         while True:
#             code = input("Enter the product code (or 'done' to finish): ").upper()
#             if code.lower() == 'DONE':
#                 break

#             if code in self._products:
#                 quantity = int(input(f"How many units of {code} do you want? "))
#                 if code in self._cart:
#                     self._cart[code] += quantity
#                 else:
#                     self._cart[code] = quantity
#             else:
#                 print("Invalid product code! Please try again!!.")

#     def generate_bill(self):
#         print("\n\n===== Your Bill =====")
#         total_amount = 0.0
#         for code, quantity in self._cart.items():
#             price = self._products[code]
#             subtotal = price * quantity
#             total_amount += subtotal
#             print(f"{code}: Rs{price:.2f} x {quantity} = Rs{subtotal:.2f}")

#         print("=====================")
#         print(f"Total Amount: Rs{total_amount:.2f}")

# if __name__ == "__main__":
#     my_store = Store()
#     my_store.display_menu()
#     my_store.take_order()
#     my_store.generate_bill()


#1. wap that has a class Store which keeps a record of code and price of each product. display the menu of all products to the user and prompt him to enter the quantity of each item required.and generate a bill and display total amount. 
class Store:
    def __init__(self):
        self.products = {} 

    def add_product(self, code, price):
        self.products[code] = price

    def display_menu(self):
        print("Product Menu:")
        for code, price in self.products.items():
            print(f"{code}: ${price}")

    def generate_bill(self, quantities):
        total_amount = 0
        print("\nYour Bill:")
        for code, quantity in quantities.items():
            if code in self.products:
                price = self.products[code]
                subtotal = price * quantity
                total_amount += subtotal
                print(f"{code}: {quantity} x Rs{price} = Rs{subtotal}")
            else:
                print(f"Invalid product code: {code}")

        print(f"\nTotal Amount: Rs{total_amount}")


def main():
    store = Store()

    store.add_product("001", 10.0)
    store.add_product("002", 20.0)
    store.add_product("003", 15.0)

    store.display_menu()

    quantities = {}
    print(""" PRODUCT CODE               PRICE
        001.Copy                Rs 10.0
        002.Scale               Rs 20.0
        003.Pen                 Rs 15.0""")
    while True:
        code = input("Enter product code (or 'done' to finish): ")
        if code.lower() == 'done':
            break
        quantity = int(input(f"Enter quantity for product {code}: "))
        quantities[code] = quantity

    store.generate_bill(quantities)


if __name__ == "__main__":
    main()
