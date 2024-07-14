from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    command = input(f"What would you like? ({menu.get_items()}): ")
    if command == "off":
        break
    elif command == "report":
        coffee_maker.report()
        money_machine.report()
    elif command not in menu.get_items():
        print("Invalid command")
    else:
        drink = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
