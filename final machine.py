from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
clear = lambda: os.system('cls')
money_machin = MoneyMachine()
coffe_machine = CoffeeMaker()
menu = Menu()

repeat = True
while repeat:
    choice = input(f"What would you like {menu.get_items()}?:")
    if choice == "off":
        clear()
        print("THE MACHINE IS CURRUTLY OFF,COME BACK SOON")
        repeat = False
    elif choice == "report":
        clear()
        print(f"Currently there is-")
        coffe_machine.report()
        money_machin.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_machine.is_resource_sufficient(drink):
            money_machin.make_payment(drink.cost)
            coffe_machine.make_coffee(drink)
        
        