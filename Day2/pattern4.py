n=int(input("enter the sie :"))
for i in range(0,n):
    for j in range(0,n):
        if(i>=j):
            print("*",end="")
    print()