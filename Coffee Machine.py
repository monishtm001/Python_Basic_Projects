#TODO: Part 1
# coffee_menu = {
#     "espresso": {
#         "water": 5,
#         "milk": 0,
#         "coffee": 1,
#         "cost": 1
#     },
#     "latte": {
#         "water": 20,
#         "milk": 15,
#         "coffee": 24,
#         "cost": 2
#     },
#     "cappuccino": {
#         "water": 25,
#         "milk": 10,
#         "coffee": 2,
#         "cost": 3
#     }
# }


# menu = input("What would you like to drink today? \nType: \nE for Espresso \nL for Latte \nC for Cappuccino  ").lower()

# while True:
#     print("USE \noff:stop the machine \nreport:to view remainings of the machine")
    
#     user_input=input("Enter:").lower()

#     if user_input=="report":
#         # Water=0
#         # Milk=0
#         # CoffeeP=0
#         # Cost=0
#         # for coffes in coffee_menu:
#         #     menues=coffee_menu[coffes]

#         #     for coff in menues:
#         #         menue_p=menues[coff]
#         #         if coff=="water":
#         #             Water+=menue_p
#         #             w_total=Water
                    
#         #         elif coff=="milk":
#         #             Milk+=menue_p
#         #             m_total=Milk
                    
#         #         elif coff=="coffee":
#         #             CoffeeP+=menue_p
#         #             cof_total=CoffeeP
                    
#         #         elif coff=="cost":
#         #             Cost+=menue_p
#         #             cos_total=Cost
                
#         # print(f"Water = {w_total}ml")
#         # print(f"Milk = {m_total}ml")
#         # print(f"Coffee Powder = {cof_total}ml")
#         # print(f"Cost= ${cos_total}")


#     elif user_input=="off":
#         print("Thank u for tasting our coffee.Come Again!!")
#         break
    
# coffee_menu = {
#     "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1},
#     "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2},
#     "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3}
# }

# menu = input("What would you like to drink today? \nE for Espresso \nL for Latte \nC for Cappuccino: ").lower()

# while True:
#     print("USE\noff: stop the machine\nreport: view remaining resources")
#     user_input = input("Enter: ").lower()

#     if user_input == "report":
#         totals = {"water": 0, "milk": 0, "coffee": 0, "cost": 0}

#         for drink in coffee_menu.values():
#             for item, value in drink.items():
#                 totals[item] += value

#         print(f"Water = {totals["water"]} ml")
#         print(f"Milk = {totals["milk"]} ml")
#         print(f"Coffee Powder = {totals["coffee"]} ml")
#         print(f"Cost = ${totals["cost"]}")

#     elif user_input == "off":
#         print("Thank you for tasting our coffee. Come again!!")
#         break





coffee_menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3}
}

menu = input("What would you like to drink today? \nE for Espresso \nL for Latte \nC for Cappuccino: ").lower()
Total_W=500
Total_M=250
Total_C=200
while True:
    print("USE\noff: stop the machine\nreport: view remaining resources")
    user_input = input("Enter: ").lower()
    if user_input == "report":
        print(f"Water:{Total_W}")
        print(f"Milk:{Total_M}")
        print(f"Coffee Powder:{Total_C}")
    elif user_input == "off":
        print("Thank you for tasting our coffee. Come again!!")
        break

# for type_of_coffee in coffee_menu.values():
#     for ingredients,items in type_of_coffee.items():