import pandas as pd
import numpy as np

# Load the .ods file into an ExcelFile object
xls = pd.ExcelFile("data.ods", engine="odf")

# Load data from all 4 sheets into separate DataFrames
sheet1 = xls.parse("Data1")
sheet2 = xls.parse("Data2")
sheet3 = xls.parse("Data3")
sheet4 = xls.parse("Data4")
sheet5 = xls.parse("Data5")

data = pd.concat([sheet1, sheet2, sheet3, sheet4, sheet5], axis=1)

# Check for duplicate column names
duplicate_columns = data.columns[data.columns.duplicated()]

# If 'duplicate_columns' is not empty, it contains the names of duplicate columns
if not duplicate_columns.empty:
    print("Duplicate columns found:")
    print(duplicate_columns)
else:
    print("No duplicate columns found")

data = data.loc[:, (data != 0).any(axis=0)] # remove all zero columns

data.replace(0, np.nan, inplace=True) # replace all 0 elements with "NaN"

print(data)

# writing consolidated data in .xlsx & .csv file
data.to_excel("fcd.xlsx", index=False)
