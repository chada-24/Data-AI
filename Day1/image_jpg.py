import os
import shutil

source ="C:/Users/spandana/Desktop/images"
backup = "C:/Users/spandana/Desktop/images_backup"


os.makedirs(backup, exist_ok=True)

for file in os.listdir(source):
    if file.lower().endswith(".jpg"):
        src_path = os.path.join(source, file)
        dst_path = os.path.join(backup, file)
        shutil.copy2(src_path, dst_path)

print("Backup completed! Only JPG files copied.")