import bill_cal

name=input("Enter your name")
phone_no=input("Enter your phone number:")
place=input("Place you have travelled to:")
bn=int(input("Enter no:of bills:"))
bills=[]
for i in range(1,bn+1):
    bill=int(input("enter bill:"))
    bills.append(bill)
        
total=bill_cal.total_bill(*bills)
list=bill_cal.profile(Name=name.title(),Phone_no=phone_no,Location=place.strip(),total_amount=total)
for i in list:
    print(i)
