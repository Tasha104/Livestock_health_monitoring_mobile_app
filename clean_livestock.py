import pandas as pd

print("✅ SCRIPT STARTED")

# Skip the first text row; use second row as header
df = pd.read_excel('Livestock_and_Meat_International_Trade.csv.xls', header=1)

print("✅ Preview of raw data:")
print(df.head())

# Drop completely empty rows and columns
df.dropna(axis=0, how='all', inplace=True)
df.dropna(axis=1, how='all', inplace=True)

# Fill missing values in numeric columns with 0
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(0)

print("✅ Columns in the file:")
print(df.columns)

# Remove any rows where 'Year' is not a number (removes footer text rows)
df = df[pd.to_numeric(df['Year'], errors='coerce').notnull()]

# Now convert 'Year' column to integer type
df['Year'] = df['Year'].astype(int)

# Optionally create a 'Date' column for easier date handling
df['Date'] = pd.to_datetime(df['Year'], format='%Y', errors='coerce')

print("✅ Cleaned Data Preview:")
print(df.head())

# Save cleaned data to CSV
df.to_csv('livestock_cleaned.csv', index=False)

print("🎉 Cleaned dataset saved as 'livestock_cleaned.csv'")
print("✅ Script finished running!")
