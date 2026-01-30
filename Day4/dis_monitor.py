import shutil

total, used, free = shutil.disk_usage("c:/")

print(f"Total Disk: {total // (1024**3)} GB")
print(f"Used Disk : {used // (1024**3)} GB")
print(f"Free Disk : {free // (1024**3)} GB")
