import pandas as pd

data = pd.read_excel("fcd.ods", engine="odf")

keywords = ["nonperform", "bank", "money", "account", "loan", "interest", "lend"]

# Create a list of column names that contain the keyword
matches = ['Years'] + [col for col in data.columns if any(keyword.lower() in col.lower() for keyword in keywords)]

# Create a new DataFrame with only the matching columns
filtered_data = data[matches]

print(filtered_data)

# Save the filtered data to an Excel file
filtered_data.to_excel("bank.xlsx", index=False)
