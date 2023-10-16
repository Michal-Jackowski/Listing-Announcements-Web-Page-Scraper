import re
import pandas as pd
import path
import datetime

print("Probability Calculator data logic here.")

# DATE AGGREGATION 
# EXAMPLE 2023-07-24 09:02
df_spot = pd.read_excel(path.filtered_data_from_webpage_spot_excel)

number_of_00_hour, number_of_01_hour, number_of_02_hour, number_of_03_hour, number_of_04_hour, number_of_05_hour, number_of_06_hour, number_of_07_hour = 0, 0, 0, 0, 0, 0, 0, 0
number_of_08_hour, number_of_09_hour, number_of_10_hour, number_of_11_hour, number_of_12_hour, number_of_13_hour, number_of_14_hour, number_of_15_hour = 0, 0, 0, 0, 0, 0, 0, 0
number_of_16_hour, number_of_17_hour, number_of_18_hour, number_of_19_hour, number_of_20_hour, number_of_21_hour, number_of_22_hour, number_of_23_hour = 0, 0, 0, 0, 0, 0, 0, 0

for x in range(len(df_spot)):
    date = df_spot["Date"][x]
    if re.search("00:", date, re.IGNORECASE):
        number_of_00_hour += 1
    elif re.search("01:", date, re.IGNORECASE):
        number_of_01_hour += 1
    elif re.search("02:", date, re.IGNORECASE):
        number_of_02_hour += 1
    elif re.search("03:", date, re.IGNORECASE):
        number_of_03_hour += 1
    elif re.search("04:", date, re.IGNORECASE):
        number_of_04_hour += 1
    elif re.search("05:", date, re.IGNORECASE):
        number_of_05_hour += 1
    elif re.search("06:", date, re.IGNORECASE):
        number_of_06_hour += 1
    elif re.search("07:", date, re.IGNORECASE):
        number_of_07_hour += 1
    elif re.search("08:", date, re.IGNORECASE):
        number_of_08_hour += 1
    elif re.search("09:", date, re.IGNORECASE):
        number_of_09_hour += 1
    elif re.search("10:", date, re.IGNORECASE):
        number_of_10_hour += 1
    elif re.search("11:", date, re.IGNORECASE):
        number_of_11_hour += 1
    elif re.search("12:", date, re.IGNORECASE):
        number_of_12_hour += 1
    elif re.search("13:", date, re.IGNORECASE):
        number_of_13_hour += 1
    elif re.search("14:", date, re.IGNORECASE):
        number_of_14_hour += 1
    elif re.search("15:", date, re.IGNORECASE):
        number_of_15_hour += 1
    elif re.search("16:", date, re.IGNORECASE):
        number_of_16_hour += 1
    elif re.search("17:", date, re.IGNORECASE):
        number_of_17_hour += 1
    elif re.search("18:", date, re.IGNORECASE):
        number_of_18_hour += 1
    elif re.search("19:", date, re.IGNORECASE):
        number_of_19_hour += 1
    elif re.search("20:", date, re.IGNORECASE):
        number_of_20_hour += 1
    elif re.search("21:", date, re.IGNORECASE):
        number_of_21_hour += 1
    elif re.search("22:", date, re.IGNORECASE):
        number_of_22_hour += 1
    elif re.search("23:", date, re.IGNORECASE):
        number_of_23_hour += 1

hours_list = {"00:00": number_of_00_hour, "01:00": number_of_01_hour, "02:00": number_of_02_hour, "03:00": number_of_03_hour, "04:00": number_of_04_hour, "05:00": number_of_05_hour, "06:00": number_of_06_hour, "07:00": number_of_07_hour,
              "08:00": number_of_08_hour, "09:00": number_of_09_hour, "10:00": number_of_10_hour, "11:00": number_of_11_hour, "12:00": number_of_12_hour, "13:00": number_of_13_hour, "14:00": number_of_14_hour, "15:00": number_of_15_hour,
              "16:00": number_of_16_hour, "17:00": number_of_17_hour, "18:00": number_of_18_hour, "19:00": number_of_19_hour, "20:00": number_of_20_hour, "21:00": number_of_21_hour, "22:00": number_of_22_hour, "23:00": number_of_23_hour}

print("All hours = " + str(hours_list))