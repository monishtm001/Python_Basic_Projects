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
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
}

# Machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resources(drink):
    for item in ["water", "milk", "coffee"]:
        if resources[item] < coffee_menu[drink][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)

def make_coffee(drink):
    for item in ["water", "milk", "coffee"]:
        resources[item] -= coffee_menu[drink][item]
    print(f"Here is your {drink}. Enjoy ☕")

# Main loop
while True:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("Machine turned off.")
        break

    elif choice == "report":
        print_report()

    elif choice in coffee_menu:
        if check_resources(choice):
            payment = process_coins()
            cost = coffee_menu[choice]["cost"]

            if payment < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(payment - cost, 2)
                if change > 0:
                    print(f"Here is ${change} dollars in change.")
                resources["money"] += cost
                make_coffee(choice)
    else:
        print("Invalid selection. Try again.")
