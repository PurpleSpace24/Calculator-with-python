import time


def coffeeMachine():
    flag = True
    order_list = []
    while flag:
        print("\n\nHello, welcome to YT Coffee!!!")
        time.sleep(0.2)

        customer_name = input("What is your name?\n")
        print("Hello, " + customer_name + ", thank you so much for coming in today.\n")
        drinks_menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappe, Ice Coffee," \
                      "Milk shake (Choose flavour - chocolate, " \
                      "vanilla, strawberry, blueberry)"

        time.sleep(0.2)
        print(
            customer_name + ", what would you like from our menu today?\nHere is what we are serving:\n" + drinks_menu)
        order = input("Enter: ")
        order_list.insert(1, order)

        time.sleep(0.31)
        print("\nSounds good " + customer_name + ", we'll have that ")
        for x in range(len(order_list)):
            print(order_list[x] + " ")

        while flag:
            time.sleep(0.31)
            answ = input("\n\nDo you need something else? y/n\n")
            if answ.lower() == 'no' or answ.lower() == 'n':
                flag = False
                break
            elif answ.lower() == 'yes' or answ.lower() == 'y':
                order = input(drinks_menu + "\nContinue: ")
                order_list.insert(1, order)
                continue

        time.sleep(0.31)

        print("------------------\nEverything " + customer_name + " ordered: ")
        for x in range(len(order_list)):
            print(order_list[x] + "")
        print("------------------\n")

        order = order_list

        time.sleep(0.31)
        print("Ready for you in a moment!")
        time.sleep(0.31)
        print("\nThank you for your order!\nYou can pay with card or cash at the cashier.\nHave a nice day! :) ")
        time.sleep(1.5)

    coffeeMachine()  # repeat function
