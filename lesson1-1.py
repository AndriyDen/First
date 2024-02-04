from pathlib import Path
import time

file_path = Path("C:/Users/Denysenko/Documents/Accounting policy_Goodyear_bilingual.docx")

# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime

print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")