import uber

name = input("Enter your name: ")

print("\nAvailable Locations:")
uber.view_location()

source = int(input("\nSelect your current location: "))

if source > len(uber.location):
    new_loc = input("Enter your current location name: ")
    uber.add_location(source, new_loc)

destination = int(input("Enter your destination location number: "))

fare = uber.calculate_fare(source, destination)
print("\nFare for your ride: ₹", fare)

confirm = input("Confirm ride [y/n]: ")

if confirm.lower() == "y":
    print("\nStatus:", uber.status[0])
    driver = uber.assign_driver(source)
    print(driver, "is arriving...")
    print("Status:", uber.status[1])

    arrived = input("\nHave you arrived at destination? [y/n]: ")

    if arrived.lower() == "y":
        feedback = input("Please give your feedback: ")

        uber.generate_invoice(
            customer_name=name,
            source=uber.location[source - 1],
            destination=uber.location[destination - 1],
            driver=driver,
            fare=fare,
            feedback=feedback
        )
    else:
        print("Ride still in progress...")
else:
    print("Status:", uber.status[3])
