import os
import pandas as pd

# Paths
folder_path = r"C:\Users\Dell\Documents\moses\BIT 321 CAT1 October 2025\scripts"
excel_path = r"C:\Users\Dell\Documents\moses\BIT 321 CAT1 October 2025\marks.xlsx"

# Read the Excel file
df = pd.read_excel(excel_path)

# Get the first column (assuming it contains filenames, without extensions)
excel_files = df.iloc[:, 0].dropna().astype(str).str.strip().tolist()

# Get the list of files in the folder (remove extensions)
folder_files = [
    os.path.splitext(f)[0]  # remove extension
    for f in os.listdir(folder_path)
    if os.path.isfile(os.path.join(folder_path, f))
]

# Find files in folder but not in Excel
missing_in_excel = [f for f in folder_files if f not in excel_files]

# Print the result
print("Files in folder (without extensions) that are not in Excel column 1:")
for f in missing_in_excel:
    print(f)

# Optionally, save to a CSV
if missing_in_excel:
    pd.DataFrame(missing_in_excel, columns=["Missing Files"]).to_csv("missing_files.csv", index=False)
    print("\nList saved to missing_files.csv")
else:
    print("\nAll files in the folder (without extensions) are listed in the Excel file.")
