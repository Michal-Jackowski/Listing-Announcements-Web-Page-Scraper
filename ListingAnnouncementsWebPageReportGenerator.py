import re
import pandas as pd
import path
import datetime

# Finish Probablity Calculator First
# Table Template is ready
print("Report generator data logic here.")

# Create a Pandas dataframe from some data.
df = pd.DataFrame(
    {
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "00:00": [0, 1, 2, 3, 4, 5, 6],
        "01:00": [0, 1, 2, 3, 4, 5, 6],
        "02:00": [0, 1, 2, 3, 4, 5, 6],
        "03:00": [0, 1, 2, 3, 4, 5, 6],
        "04:00": [0, 1, 2, 3, 4, 5, 6],
        "05:00": [0, 1, 2, 3, 4, 5, 6],
        "06:00": [0, 1, 2, 3, 4, 5, 6],
        "07:00": [0, 1, 2, 3, 4, 5, 6],
        "08:00": [0, 1, 2, 3, 4, 5, 6],
        "09:00": [0, 1, 2, 3, 4, 5, 6],
        "10:00": [0, 1, 2, 3, 4, 5, 6],
        "11:00": [0, 1, 2, 3, 4, 5, 6],
        "12:00": [0, 1, 2, 3, 4, 5, 6],
        "13:00": [0, 1, 2, 3, 4, 5, 6],
        "14:00": [0, 1, 2, 3, 4, 5, 6],
        "15:00": [0, 1, 2, 3, 4, 5, 6],
        "16:00": [0, 1, 2, 3, 4, 5, 6],
        "17:00": [0, 1, 2, 3, 4, 5, 6],
        "18:00": [0, 1, 2, 3, 4, 5, 6],
        "19:00": [0, 1, 2, 3, 4, 5, 6],
        "20:00": [0, 1, 2, 3, 4, 5, 6],
        "21:00": [0, 1, 2, 3, 4, 5, 6],
        "22:00": [0, 1, 2, 3, 4, 5, 6],
        "23:00": [0, 1, 2, 3, 4, 5, 6],
    }
)

# Order the columns if necessary.
df = df[["Day", "00:00", "01:00", "02:00", "03:00", "04:00",
         "05:00", "06:00", "07:00", "08:00", "09:00", "10:00",
         "11:00", "12:00", "13:00", "14:00", "15:00", "16:00",
         "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", 
         "23:00"]]
writer = pd.ExcelWriter(path.spot_raport_excel, engine="xlsxwriter")

# Write the dataframe data to XlsxWriter. Turn off the default header and
# index and skip one row to allow us to insert a user defined header.
df.to_excel(writer, sheet_name="Sheet1", startrow=1, header=False, index=False)

workbook = writer.book
worksheet = writer.sheets["Sheet1"]

# Get the dimensions of the dataframe.
(max_row, max_col) = df.shape

# Create a list of column headers, to use in add_table().
column_settings = [{"header": column} for column in df.columns]

# Add the Excel table structure. Pandas will add the data.
worksheet.add_table(0, 0, max_row, max_col - 1, {"columns": column_settings})

# Make the columns wider for clarity.
worksheet.set_column(0, max_col - 1, 12)

writer.close()
print("Saving to the xlsx file was successful.")