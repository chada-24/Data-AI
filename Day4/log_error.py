error_address=[]

with open("sample_logs.log","r") as log:
    lines=log.readlines()
    
    for line in lines:
        if "ERROR" in line:
            words=line.split("]")
            error=words[2]
            error_address.append(error)
            
with open("error_logs.txt","w") as ip:
    for addr in error_address:
        ip.write(addr+"\n")
        
print("Error extract successfully")
    