import re
import pandas as pd
import path
import datetime
import ListingAnnouncementsWebPageProbabilityCalculator
import ColorScalesInExcel

def create_dataframe():
    df = pd.DataFrame(
        {
            "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "00:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "01:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "02:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "03:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "04:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "05:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "06:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "07:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "08:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "09:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "10:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "11:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "12:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "13:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "14:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "15:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "16:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "17:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "18:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "19:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "20:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "21:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "22:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
            "23:00": [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
        }
    )
    return df

# To avoid warning spam
pd.options.mode.chained_assignment = None
probability_lists = ListingAnnouncementsWebPageProbabilityCalculator.get_probability_results()
hour_list = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
df = create_dataframe()
df1 = create_dataframe()
df2 = create_dataframe()
empty_df_list = [df, df1, df2]
sum_list = [0, 0, 0]
sum = 0
i = 0

for probability_list in probability_lists:
    key_list = probability_list.keys()
    for key in key_list:
        for hour in hour_list:
            sum += int(probability_list[key][hour])
    if i == 0:
        sum_list[i] = sum
    elif i == 1:
        sum_list[i] = sum
    elif i == 2:
        sum_list[i] = sum
    sum = 0
    i += 1

for probability_list, dff, sum in zip(probability_lists, empty_df_list, sum_list):
    key_list = probability_list.keys()
    for key in key_list:
        for hour in hour_list:
            if probability_list[key][hour] != 0:
                if key == "Monday":
                    dff[hour][0] = (probability_list[key][hour] / sum)
                elif key == "Tuesday":
                    dff[hour][1] = (probability_list[key][hour] / sum)
                elif key == "Wednesday":
                    dff[hour][2] = (probability_list[key][hour] / sum)
                elif key == "Thursday":
                    dff[hour][3] = (probability_list[key][hour] / sum)
                elif key == "Friday":
                    dff[hour][4] = (probability_list[key][hour] / sum)
                elif key == "Saturday":
                    dff[hour][5] = (probability_list[key][hour] / sum)
                elif key == "Sunday":
                    dff[hour][6] = (probability_list[key][hour] / sum)

# Order the columns if necessary.
df = df[["Day", "00:00", "01:00", "02:00", "03:00", "04:00",
         "05:00", "06:00", "07:00", "08:00", "09:00", "10:00",
         "11:00", "12:00", "13:00", "14:00", "15:00", "16:00",
         "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", 
         "23:00"]]

excel_files_list = [path.spot_raport_excel, path.futures_raport_excel, path.others_raport_excel]
df_list = [df, df1, df2]
for x, dff in zip(excel_files_list, df_list):
    writer = pd.ExcelWriter(x, engine="xlsxwriter")

    # Write the dataframe data to XlsxWriter. Turn off the default header and
    # index and skip one row to allow us to insert a user defined header.
    dff.to_excel(writer, sheet_name="Sheet1", startrow=1, header=False, index=False)

    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]

    # Get the dimensions of the dataframe.
    (max_row, max_col) = dff.shape

    # Create a list of column headers, to use in add_table().
    column_settings = [{"header": column} for column in dff.columns]

    # Add the Excel table structure. Pandas will add the data.
    worksheet.add_table(0, 0, max_row, max_col - 1, {"columns": column_settings})

    # Make the columns wider for clarity.
    worksheet.set_column(0, max_col - 1, 12)
    # Add a percent number format.
    percent_format = workbook.add_format({"num_format": "0.00%"})

    # Apply the number format to Grade column.
    worksheet.set_column('B2:Y8', None, percent_format)

    # Adding Colors scales to cells
    for x in hour_list:
        ColorScalesInExcel.conditional_color_column(worksheet, dff, x)

    writer.close()
    print("Saving to the xlsx file was successful.")