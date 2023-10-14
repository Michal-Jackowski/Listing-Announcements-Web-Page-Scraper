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
df = pd.read_excel(path.scraped_data_from_webpage_excel)

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
    if re.search("Binance Futures Will List", text, re.IGNORECASE):
        df_futures = df_futures._append(temp_df)

writer = pd.ExcelWriter(path.filtered_data_from_webpage_spot_excel.format(datetime.date.today()), engine='xlsxwriter')
writer2 = pd.ExcelWriter(path.filtered_data_from_webpage_futures_excel.format(datetime.date.today()), engine='xlsxwriter')
df_spot.to_excel(writer, sheet_name="MySheet", index=False)
df_futures.to_excel(writer2, sheet_name="MySheet", index=False)

workbook = writer.book
worksheet = writer.sheets['MySheet']
workbook2 = writer2.book
worksheet2 = writer2.sheets['MySheet']

for i, col in enumerate(df_spot.columns):
    width = max(df_spot[col].apply(lambda x: len(str(x))).max(), len(col))
    worksheet.set_column(i, i, width)

for i, col in enumerate(df_futures.columns):
    width = max(df_futures[col].apply(lambda x: len(str(x))).max(), len(col))
    worksheet2.set_column(i, i, width)

writer._save()
writer2._save()
print("Saving to the xlsx file was successful.")