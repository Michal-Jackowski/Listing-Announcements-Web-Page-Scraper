import re
import pandas as pd
import path
import datetime
#from ListingAnnouncementsWebPageScraper import df, df3

print("Filter data logic here.")

df = pd.DataFrame()
df3 = pd.DataFrame()
data = pd.DataFrame()
df_spot = pd.DataFrame()
df_futures = pd.DataFrame()
df_others = pd.DataFrame()
df = pd.read_excel(path.scraped_data_from_webpage_excel)

number_of_00_hour, number_of_01_hour, number_of_02_hour, number_of_03_hour, number_of_04_hour, number_of_05_hour, number_of_06_hour, number_of_07_hour = 0, 0, 0, 0, 0, 0, 0, 0
number_of_08_hour, number_of_09_hour, number_of_10_hour, number_of_11_hour, number_of_12_hour, number_of_13_hour, number_of_14_hour, number_of_15_hour = 0, 0, 0, 0, 0, 0, 0, 0
number_of_16_hour, number_of_17_hour, number_of_18_hour, number_of_19_hour, number_of_20_hour, number_of_21_hour, number_of_22_hour, number_of_23_hour = 0, 0, 0, 0, 0, 0, 0, 0

if(df3.empty):
    data = df.copy()
else:
    data = df3.copy()

for x in range(len(data)):
    date = data["Date"][x]
    text = data["Article Header"][x]
    filtered_data = {"Date" : str(data["Date"][x]), "Article Header" : str(data["Article Header"][x])}
    temp_df = pd.DataFrame(filtered_data, index=[1])
    # SPOT LISTINGS
    if re.search("Binance List", text, re.IGNORECASE):
        df_spot = df_spot._append(temp_df)
    elif re.search("Binance Lists", text, re.IGNORECASE):
        df_spot = df_spot._append(temp_df)
    elif re.search("Binance Will List", text, re.IGNORECASE):
        df_spot = df_spot._append(temp_df)
    # FUTURES LISTINGS
    elif re.search("Binance Futures Will Launch", text, re.IGNORECASE):
        df_futures = df_futures._append(temp_df)
    elif re.search("Binance Futures Will List", text, re.IGNORECASE):
        df_futures = df_futures._append(temp_df)
    else:
        df_others = df_others._append(temp_df)
    # DATE AGGREGATION 
    # EXAMPLE 2023-07-24 09:02
for x in range(len(df_spot)):
    text = df_spot["Date"][x]
    print("testowanie = " + str(text))
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

hours_list = [number_of_00_hour, number_of_01_hour, number_of_02_hour, number_of_03_hour, number_of_04_hour, number_of_05_hour, number_of_06_hour, number_of_07_hour,
              number_of_08_hour, number_of_09_hour, number_of_10_hour, number_of_11_hour, number_of_12_hour, number_of_13_hour, number_of_14_hour, number_of_15_hour,
              number_of_16_hour, number_of_17_hour, number_of_18_hour, number_of_19_hour, number_of_20_hour, number_of_21_hour, number_of_22_hour, number_of_23_hour]
print("All hours = " + str(hours_list))
writer = pd.ExcelWriter(path.filtered_data_from_webpage_spot_excel.format(datetime.date.today()), engine='xlsxwriter')
writer2 = pd.ExcelWriter(path.filtered_data_from_webpage_futures_excel.format(datetime.date.today()), engine='xlsxwriter')
writer3 = pd.ExcelWriter(path.filtered_data_from_webpage_others_excel.format(datetime.date.today()), engine='xlsxwriter')
df_spot.to_excel(writer, sheet_name="MySheet", index=False)
df_futures.to_excel(writer2, sheet_name="MySheet", index=False)
df_others.to_excel(writer3, sheet_name="MySheet", index=False)
worksheet = writer.sheets['MySheet']
worksheet2 = writer2.sheets['MySheet']
worksheet3 = writer3.sheets['MySheet']

df_list = [df_spot, df_futures, df_others]
worksheets = [worksheet, worksheet2, worksheet3]
writers = [writer, writer2, writer3]
for df, ws, wr in zip(df_list, worksheets, writers):
    for i, col in enumerate(df.columns):
        width = max(df[col].apply(lambda x: len(str(x))).max(), len(col))
        ws.set_column(i, i, width)
    wr._save()
print("Saving to the xlsx file was successful.")