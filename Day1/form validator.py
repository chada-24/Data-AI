e_name=str(input("enter mail_adress:"))
password=str(input("enter password"))
name=str(input("enter name:"))
age=int(input("enter age:"))
if('@' not in e_name):
    print("invalid user name")
elif (len(password)<6):
    print("invalid password")
else:
    print("sucessful")