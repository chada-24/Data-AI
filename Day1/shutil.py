import shutil
import datetime

source="C:/Users/spandana/Desktop/python/data.txt"
backup=f"C:/Users/spandana/Desktop/python/data_backup_{datetime.date.today()}.txt"

shutil.copy(source, backup)
print(f"Backup of {source} created ay {backup}")