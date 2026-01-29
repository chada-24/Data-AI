
location = ["Hyderabad", "Bangalore", "Chennai", "Pune"]

drivers = ["Rakesh", "Uday", "John", "Ali"]

status = ("waiting", "ride started", "completed", "canceled")

distance = {
    (1, 2): 500,
    (1, 3): 630,
    (1, 4): 560,
    (2, 3): 350,
    (2, 4): 840,
    (3, 4): 1200
}

def view_location():
    for i in range(len(location)):
        print(i + 1, ".", location[i])


def add_location(pos, loc_name, driver_name):
    location.insert(pos - 1, loc_name)
    drivers.insert(pos - 1, driver_name)



def calculate_fare(src, dest):
    key = (src, dest)
    if key not in distance:
        key = (dest, src)
    dist = distance.get(key, 300)
    return dist * 2


def assign_driver(index):
    return drivers[index - 1]


def generate_invoice(**kwargs):
    print("\n========== INVOICE ==========")
    for key, value in kwargs.items():
        print(key.capitalize(), ":", value)
    print("Ride Status :", status[2])
    print("=============================")
