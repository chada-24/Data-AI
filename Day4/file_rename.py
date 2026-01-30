import os

path = "C:/Users/spandana/Desktop/images_backup"

for count, filename in enumerate(os.listdir(path), start=1):
    old_path = os.path.join(path, filename)
    new_path = os.path.join(path, f"file_{count}.jpg")
    os.rename(old_path, new_path)

print("Files renamed successfully")
