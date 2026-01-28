# n=int(input("enter the sie :"))
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==0 or i==n-1 or (i+j)==n-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()



a=[]
while True:
    item=input("enter an item:")
    if(item in "done"):
        break
    else:
        a.append(item)
        
print(a)