
menu = {
    1: ("Burger", 120),
    2: ("Pizza", 250),
    3: ("Pasta", 180),
    4: ("Sandwich", 100),
    5: ("Cold Drink", 60)
}

def calculate_bill(order_list, *quantities, **charges):
    total = 0

    for i in range(len(order_list)):
        item_price = order_list[i][1]
        total += item_price * quantities[i]

    delivery = charges.get("delivery", 0)
    tax = charges.get("tax", 0)
    discount = charges.get("discount", 0)

    total = total + delivery + tax - discount
    return total

def zomato_order():
    order_items = []   # list
    quantities = []    # list

    try:
        print("\nZOMATO MENU")
        for key, value in menu.items():
            print(f"{key}. {value[0]} - ₹{value[1]}")

        while True:
            try:
                choice = int(input("\nEnter item number (0 to finish): "))

                if choice == 0:
                    break

                if choice not in menu:
                    raise ValueError("Invalid menu choice")

                qty = int(input("Enter quantity: "))
                if qty <= 0:
                    raise ValueError("Quantity must be positive")

                order_items.append(menu[choice])
                quantities.append(qty)

            except ValueError as ve:
                print("Input Error:", ve)

        if not order_items:
            raise Exception("No items selected")

        delivery_charge = 40
        tax = 30
        discount = 50 if len(order_items) >= 3 else 0

        bill = calculate_bill(
            order_items,
            *quantities,
            delivery=delivery_charge,
            tax=tax,
            discount=discount
        )

    except Exception as e:
        print("\n Order Failed:", e)

    else:
        print("\n ORDER SUMMARY")
        for i in range(len(order_items)):
            name, price = order_items[i]
            print(f"{name} x {quantities[i]} = ₹{price * quantities[i]}")

        print(f"Delivery Charge: ₹{delivery_charge}")
        print(f"Tax: ₹{tax}")
        print(f"Discount: ₹{discount}")
        print(f"\n Total Bill Amount: ₹{bill}")

    finally:
        print("\n Thank you for ordering from Zomato!")

zomato_order()
