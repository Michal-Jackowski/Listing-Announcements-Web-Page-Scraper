import re
import pandas as pd
import path
import datetime

print("Filter data logic here.")

df = pd.DataFrame()
df3 = pd.DataFrame()
data = pd.DataFrame()
df_spot = pd.DataFrame()
df_futures = pd.DataFrame()
df_others = pd.DataFrame()
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
    elif re.search("Binance Futures Will List", text, re.IGNORECASE):
        df_futures = df_futures._append(temp_df)
    else:
        df_others = df_others._append(temp_df)

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