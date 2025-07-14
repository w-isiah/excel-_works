import pandas as pd

# File path
file_path = r'D:\python\excel works\mine.xlsx'

# Load the Excel file
df = pd.read_excel(file_path)

# Optional: Preview the data
print("📄 Excel File Preview:")
print(df.head())
print("\n📑 Column Names:")
print(df.columns)

# Correct splitting function
def split_name(full_name):
    parts = str(full_name).strip().split()
    last = parts[0] if len(parts) > 0 else ''
    first = parts[1] if len(parts) > 1 else ''
    others = ' '.join(parts[2:]) if len(parts) > 2 else ''
    return pd.Series([last, first, others])

# Apply to correct column
df[['Last Name', 'First Name', 'Other Name']] = df['NAME OF PUPIL'].apply(split_name)

# Optional: Replace NaN with empty string
df = df.fillna('')

# Save the result
df.to_excel(r'D:\python\excel works\separated.xlsx', index=False)

print("✅ Done! File saved as 'separated.xlsx'")