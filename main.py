



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

# TODO 1 - Print report of all coffee machine resources

# TODO Check resources are sufficient to create a coffee machine

def is_resources_sufficient(order_ingredients):
    """Return True when order can be made sufficient, and return false when order ingredients insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

def process_coin():
    """This Function return total calculated from coin inserted"""
    print("Please Enter the Coin: ")
    total = int(input("How Many Quarters?: ")) *0.25   # To Convert it into Dolor
    total += int(input("How Many dimes?: ")) * 0.1
    total += int(input("How Many Nickles?: ")) * 0.05
    total += int(input("How Many Pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True if payment accepted or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost

        return True
    else:
        print(f"Sorry there is not enough Money, money refunded.{round(money_received,2)}")
        return False

def make_coffee(drink_name, order_ingredients):
    """This Function make a coffee with drink name and ingredients"""
    """Also Deduct the required ingredients from the resources dictionary"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}'s coffee ☕︎")



profit = 0

resources ={
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_On = True

while is_On:

    choice  = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_On = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resources_sufficient(drink["ingredients"]):
            payment =process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
