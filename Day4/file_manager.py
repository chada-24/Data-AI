import os
import shutil

source_folder =r"C:\Users\spandana\Desktop\anjali"

main_folder ="C:/Users/spandana/Desktop/Organized_Files"

folders = {
    "PDFs": [".pdf"],
    "Word_Documents": [".doc", ".docx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"]
}

os.makedirs(main_folder, exist_ok=True)

for folder in folders:
    os.makedirs(os.path.join(main_folder, folder), exist_ok=True)


for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        for folder, extensions in folders.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(
                    file_path,
                    os.path.join(main_folder, folder, file)
                )

print("Files organized successfully")
