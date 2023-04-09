"""Code without using OOP"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
power = "on"


def main():
    def check_resources(choice):
        truth = []
        for j in MENU[choice]["ingredients"]:
            if resources[j] > MENU[choice]["ingredients"][j]:
                truth.append(1)
            else:
                print("not enough " + j)
                truth.append(0)
        if 0 in truth:
            print("not enough resources")
            return False
        elif 0 not in truth:
            return True

    def total_given():
        tot = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
        return tot

    def change():
        return tot - MENU[choice]["cost"]

    def edit_resources():
        global resources
        for k in resources:
            resources[k] -= MENU[choice]["ingredients"][k]

    choice = input("what would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        global power
        power = "off"
    elif choice == "report":
        for i in resources:
            print(i, resources[i])
            global profit
        print("$", profit)

    enough = check_resources(choice)

    if enough:
        sufficient = False
        while not sufficient:
            print(f"please insert coins for {MENU[choice]['cost']}$")
            q = int(input("how many quarters? "))
            d = int(input("how many dimes? "))
            n = int(input("how many nickels? "))
            p = int(input("how many pennies? "))
            tot = total_given()
            if tot >= MENU[choice]["cost"]:
                print("Here's your change ", round(change(), 2))
                print(f"Here's your {choice} enjoy!")
                sufficient = True
                edit_resources()
                profit += MENU[choice]["cost"]
            else:
                print("You didn't enter enough money")
                sufficient = False
                return main()




while power == "on":
    main()
