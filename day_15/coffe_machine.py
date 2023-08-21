from data import resources, MENU


def check_ingredients(coffe_name):
    menu_contain = MENU[coffe_name]["ingredients"]
    for i in resources:
        if resources[i] < menu_contain[i]: 
            return f"Sorry there is not enough {i}"
    return True


def update_resorce(coffe):
    coffe_ingrediends = MENU[coffe]["ingredients"]
    global resources
    for i in coffe_ingrediends:
        resources[i] -= coffe_ingrediends[i]


def check_cost():
    quarter = int(input('how many quarter :'))
    dimes = int(input('how many dimes :'))
    nickel = int(input('how many nickel :'))
    pennies = int(input('how many pennies :'))    
    return ((0.25 * quarter) + (0.10 * dimes) + (0.05 * nickel) + (0.01 * pennies))


def coffe_maker():
    coffe = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if coffe == 'off':
        print("shutdown")
    elif coffe == "report":
        print(resources)
        coffe_maker()
    elif coffe in ["espresso", "latte", "cappuccino"]:
        if check_ingredients(coffe_name=coffe) == True:
            cost = MENU[coffe]['cost'] 
            print(f"{coffe} cost: {cost}")
            totall = check_cost()
            print(f"You inserted total: {totall}")
            if totall >= cost:
                change = round(totall - cost, 4)
                print(f"Here is your change: ${change}")
                update_resorce(coffe)
                print(f"Enjoy your {coffe} ☕")
                coffe_maker()
            else:
                print("Sorry, not enough money inserted.")
                coffe_maker()
        else:
            print(check_ingredients(coffe_name=coffe))
            coffe_maker()
    else:
        print("Invalid input. Please choose from 'espresso', 'latte', 'cappuccino', or 'off'.")
        coffe_maker()


coffe_maker()
