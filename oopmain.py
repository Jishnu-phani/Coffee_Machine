"""Code with using OOP"""
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
power_on = True

while power_on:

    x = None

    order = input(f"What would you like today? {menu.get_items()}")

    if order == "off":
        power_on = False

    elif order == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(order)
        x = coffee_maker.is_resource_sufficient(drink)
        if x:
            sufficient = False
            while not sufficient:
                print(f"To pay: {drink.cost}$")
                y = money_machine. make_payment(drink.cost)
                sufficient = y
            coffee_maker.make_coffee(drink)

