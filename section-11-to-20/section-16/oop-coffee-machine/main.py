from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()

while True:
    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if choice == "off":
        break

    if choice == "report":
        coffeeMaker.report()
        moneyMachine.report()

    if choice in menu.get_items():
        drink = menu.find_drink(choice)
        if (moneyMachine.make_payment(drink.cost)
                and coffeeMaker.is_resource_sufficient(drink)):
            coffeeMaker.make_coffee(drink)

