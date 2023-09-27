import datetime
import pandas as pd
import path

df = pd.DataFrame()

#data = {"date" : x, "text" : y,}
#temp_df = pd.DataFrame(data, index=[1])
#df = df._append(temp_df)
                
#df['date'] = df['date'].dt.tz_localize(None)
#writer = pd.ExcelWriter(path.scraped_data_from_telegram.format(datetime.date.today()), engine='xlsxwriter')
#df.to_excel(writer, sheet_name="MySheet", index=False)

#workbook = writer.book
#worksheet = writer.sheets['MySheet']

#for i, col in enumerate(df.columns):
    #width = max(df[col].apply(lambda x: len(str(x))).max(), len(col))
    #worksheet.set_column(i, i, width)

#writer._save()