def mask_phone(phone):
    return phone[:2] + "******" + phone[-2:]

def calculate_total(bills):
    return sum(bills)

def is_frequent_place(place, frequent_places):
    for city in frequent_places:
        if city in place:
            return True
    return False

def extract_and_display(**kwargs):
    bills = []
    place = ""
    print("\n----- CUSTOMER DETAILS -----")
    for key, value in kwargs.items():
        if key == "phone_no":
            value = mask_phone(value)
        if key in ("travelling", "stay", "restaurant", "other_bill"):
            bills.append(value)
        if key == "place":
            place = value
        print(f"{key.capitalize()} : {value}")
    return bills, place

def billcal(**kwargs):
    frequent_places = ["Goa", "Hyderabad", "Bangalore", "Chennai"]
    bills, place = extract_and_display(**kwargs)
    total = calculate_total(bills)
    frequent = is_frequent_place(place, frequent_places)
    discount = 0
    customer_type = "Regular Customer"
    if total >= 7000:
        customer_type = "Valuable Customer"
        discount = 15 if frequent else 10
    elif frequent:
        discount = 5
    discount_amount = (discount * total) / 100
    final_amount = total - discount_amount
    print("\n----- BILL SUMMARY -----")
    print("Customer Type :", customer_type)
    print("Total Bill    :", total)
    print("Discount      :", discount, "%")
    print("Final Amount  :", final_amount)
    print("------------------------")
