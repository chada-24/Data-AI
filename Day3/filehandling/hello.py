# file=open("notes.txt","w")
# file.write("welcome to python filehadling!\n")
# file.write("this is asample file")
# file.close()

# file=open("notes.txt")
# content=file.read()
# print(content)
# file.close

# file=open("notes.txt","a")
# file.write("this is appended line\n")
# file.close

# with open("notes.txt","r") as file:
#     content=file.read()
#     print(content)
    
# feedback=input("please provide your feedback")
# with open ("feedback.txt","a") as file:
#     file.write(feedback+"\n")
# print("thank you for feedback!")

# with open("data.txt","r") as file:
#     print(file.readline().strip())
#     print(file.readline().strip())
#     print(file.readline().strip())
#     print(file.readline().strip())

with open("data.txt","r") as file:
    while True:
        line=file.readline()
        if not line:
            break
        print(line.strip())
        
