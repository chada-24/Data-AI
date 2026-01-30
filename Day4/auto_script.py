import shutil
import datetime

source = "C:/Users/spandana/Desktop/python/day4/sample_txt.txt"
backup = f"C:/Users/spandana/Desktop/python/day4/data_backup_{datetime.date.today()}.txt"

shutil.copy(source, backup)
print("Backup created successfully")
