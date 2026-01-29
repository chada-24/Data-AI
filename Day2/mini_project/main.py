import billing

name = input("Enter customer name: ")
phone = input("Enter phone number: ")
place = input("Enter place: ")
travelling = int(input("Enter travelling charge: "))
stay = int(input("Enter stay charge: "))
restaurant = int(input("Enter restaurant bill: "))
other = int(input("Enter other bill amount (0 if none): "))
billing.billcal(
    name=name,
    phone_no=phone,
    place=place,
    travelling=travelling,
    stay=stay,
    restaurant=restaurant,
    other_bill=other
)
