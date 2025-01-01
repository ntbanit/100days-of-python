import data

MENU_ORDER = data.MENU
resources = data.resources
total_money = 0
COINS = {
    "quarters" : 0.25,
    "dimes" : 0.1,
    "nickles" : 0.05,
    "pennies" : 0.01
}

def report():
    print(f"""
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${total_money}
    """)

def check_resources(order_name):
    required = MENU_ORDER[order_name]["ingredients"]
    for element in required:
        if resources[element] < required[element]:
            print(f"Sorry there is not enough {element}.")
            return False
    return True

def process_transaction(order_name):
    inserted_money = 0
    print("Please insert coins.")
    for coin in COINS:
        number = int(input(f"How many {coin}?: "))
        inserted_money += number * COINS[coin]
    cost = MENU_ORDER[order_name]["cost"]
    if inserted_money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    global total_money
    total_money += cost
    if inserted_money > cost :
        print(f"Here is ${round(inserted_money - cost, 2)} dollars in change.")
    return True

def make_coffee(order_name):
    required = MENU_ORDER[order_name]["ingredients"]
    for element in required:
        resources[element] -= required[element]
    print(f"Here is your {order_name}. Enjoy!")

def run_coffee_machine():
    global total_money
    total_money = 0
    while True:
        prompt = input("What would you like? (espresso/latte/cappuccino):")
        if prompt == "off" :
            break
        if prompt == "report" :
            report()
            continue
        if prompt in MENU_ORDER :
            if check_resources(prompt) and process_transaction(prompt) :
                make_coffee(prompt)

run_coffee_machine()


