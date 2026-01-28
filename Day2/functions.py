# name="Chada Anjali"
# initial="".join([word[0].upper() for word in name.split()])
# print(initial)
# print(name.split())


# marks=int(input("enter the marks:"))
# attendance=int(input("enter the attendance percentage:"))
# if marks>50 and attendance>75:
#     print("eligible")
# else:
#     print("not eligible")

#spend>1000 in weekend and gold offer of 20% on bill
# bill=int(input("bill:"))
# member=input("membership:")
# day=input("day:")
# if bill>1000 and member=="gold" and day in ["saturday","sunday"]:
#     bill=bill*0.8
# print(bill)

#login attempts 
# a=[]
# while True:
#     item=input("enter an item:")
#     if(item in "done"):
#         break
#     else:
#         a.append(item)
        
# print(a)
    
#profile generator 
# def profile_generator(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key.capitalize():15}: {value}")
   
# profile_generator(name="Anjali",age=21,email="anjali@gmail.com",city="Hyderabad")
# profile_generator(name="Pooja",age=23,college="CMR Engineering College",course="Computer Science")

def add_bill(*args):
    sum = 0
    for bill in args:
        sum += bill
    return sum


def billcal(**kwargs):
    bills=[]
    for key,value in kwargs.items():
        if key=="phone_no":
            value=value[:2] + "******" + value[-2:]
        if key in ["travelling_charge", "stay", "restarunt","other_bill"]:
            bills.append(value)
        print(f"{key.capitalize()} : {value}")

    total = add_bill(*bills)
    print(f"Total Bill : {total}")
    print("---------------------------------")


billcal(name="Anjali",phone_no="8328540984",place="Hyderabad",travelling_charge=2000,stay=1200,restarunt=2500)
billcal(name="Prvallika",phone_no="9768932817",place="Goa",travelling_charge=2500,stay=5000,restarunt=3000,other_bill=500)


