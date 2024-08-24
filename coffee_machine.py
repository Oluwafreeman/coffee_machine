

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("Insert quartes ")) * 0.25
    total += int(input("Insert dimes ")) * 0.1
    total += int(input("Insert nickels ")) * 0.05
    total += int(input("Insert penniess ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry there is no enough money. money refunded")
        return False
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}🥫")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False
    
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])