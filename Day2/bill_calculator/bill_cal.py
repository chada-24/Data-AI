def total_bill(*args):
    sum = 0
    for b in args:
        sum += b
    return sum


def profile(**kwargs):
    bills=[]
    for key,value in kwargs.items():
        if key=="phone_no":
            value=value[:2] + "******" + value[-2:]
        bills.append(f"{key.capitalize()} : {value}")
    return bills


