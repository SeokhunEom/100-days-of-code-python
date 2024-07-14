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
    "money": 0,
}

# coffee emoji:  ☕


def check_resources(drink):
    for key, value in drink["ingredients"].items():
        if resources[key] < value:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def make_drink(menu):
    drink = MENU[menu]
    if not check_resources(drink):
        return

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total < drink["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return

    resources["money"] += drink["cost"]
    for key, value in drink["ingredients"].items():
        resources[key] -= value
    change = round(total - drink["cost"], 2)
    print(f"Here is ${change} in change.")

    print(f"Here is your {menu} ☕. Enjoy!")


while True:
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if command == 'off':
        break
    elif command == 'report':
        for key, value in resources.items():
            print(f"{key}: {value}")
    elif command == 'espresso' or command == 'latte' or command == 'cappuccino':
        make_drink(command)
    else:
        print("Invalid command")





