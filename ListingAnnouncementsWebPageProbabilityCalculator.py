import re
import pandas as pd
import path
from datetime import datetime
import calendar

def check_hour_probability(data):    
    number_of_appearances_a_given_day = {"Monday": {"00:00": 0, "01:00": 0, "02:00": 0, "03:00": 0, "04:00": 0, "05:00": 0, "06:00": 0, "07:00": 0, "08:00": 0, "09:00": 0, "10:00": 0, "11:00": 0, "12:00": 0, "13:00": 0, "14:00": 0, "15:00": 0, "16:00": 0, "17:00": 0, "18:00": 0, "19:00": 0, "20:00": 0, "21:00": 0, "22:00": 0, "23:00": 0},
                                         "Tuesday": {"00:00": 0, "01:00": 0, "02:00": 0, "03:00": 0, "04:00": 0, "05:00": 0, "06:00": 0, "07:00": 0, "08:00": 0, "09:00": 0, "10:00": 0, "11:00": 0, "12:00": 0, "13:00": 0, "14:00": 0, "15:00": 0, "16:00": 0, "17:00": 0, "18:00": 0, "19:00": 0, "20:00": 0, "21:00": 0, "22:00": 0, "23:00": 0},
                                         "Wednesday": {"00:00": 0, "01:00": 0, "02:00": 0, "03:00": 0, "04:00": 0, "05:00": 0, "06:00": 0, "07:00": 0, "08:00": 0, "09:00": 0, "10:00": 0, "11:00": 0, "12:00": 0, "13:00": 0, "14:00": 0, "15:00": 0, "16:00": 0, "17:00": 0, "18:00": 0, "19:00": 0, "20:00": 0, "21:00": 0, "22:00": 0, "23:00": 0},
                                         "Thursday": {"00:00": 0, "01:00": 0, "02:00": 0, "03:00": 0, "04:00": 0, "05:00": 0, "06:00": 0, "07:00": 0, "08:00": 0, "09:00": 0, "10:00": 0, "11:00": 0, "12:00": 0, "13:00": 0, "14:00": 0, "15:00": 0, "16:00": 0, "17:00": 0, "18:00": 0, "19:00": 0, "20:00": 0, "21:00": 0, "22:00": 0, "23:00": 0},
                                         "Friday": {"00:00": 0, "01:00": 0, "02:00": 0, "03:00": 0, "04:00": 0, "05:00": 0, "06:00": 0, "07:00": 0, "08:00": 0, "09:00": 0, "10:00": 0, "11:00": 0, "12:00": 0, "13:00": 0, "14:00": 0, "15:00": 0, "16:00": 0, "17:00": 0, "18:00": 0, "19:00": 0, "20:00": 0, "21:00": 0, "22:00": 0, "23:00": 0},
                                         "Saturday": {"00:00": 0, "01:00": 0, "02:00": 0, "03:00": 0, "04:00": 0, "05:00": 0, "06:00": 0, "07:00": 0, "08:00": 0, "09:00": 0, "10:00": 0, "11:00": 0, "12:00": 0, "13:00": 0, "14:00": 0, "15:00": 0, "16:00": 0, "17:00": 0, "18:00": 0, "19:00": 0, "20:00": 0, "21:00": 0, "22:00": 0, "23:00": 0},
                                         "Sunday": {"00:00": 0, "01:00": 0, "02:00": 0, "03:00": 0, "04:00": 0, "05:00": 0, "06:00": 0, "07:00": 0, "08:00": 0, "09:00": 0, "10:00": 0, "11:00": 0, "12:00": 0, "13:00": 0, "14:00": 0, "15:00": 0, "16:00": 0, "17:00": 0, "18:00": 0, "19:00": 0, "20:00": 0, "21:00": 0, "22:00": 0, "23:00": 0}}

    for x in range(len(data)):
        date = data["Date"][x]
        datetime_object = datetime.strptime(date, '%Y-%m-%d %H:%M')
        day_of_week = calendar.day_name[datetime_object.weekday()]
        if re.search("00:", date, re.IGNORECASE):                
            number_of_appearances_a_given_day[day_of_week]["00:00"] += 1
        elif re.search("01:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["01:00"] += 1
        elif re.search("02:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["02:00"] += 1
        elif re.search("03:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["03:00"] += 1
        elif re.search("04:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["04:00"] += 1
        elif re.search("05:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["05:00"] += 1
        elif re.search("06:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["06:00"] += 1
        elif re.search("07:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["07:00"] += 1
        elif re.search("08:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["08:00"] += 1
        elif re.search("09:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["09:00"] += 1
        elif re.search("10:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["10:00"] += 1
        elif re.search("11:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["11:00"] += 1
        elif re.search("12:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["12:00"] += 1
        elif re.search("13:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["13:00"] += 1
        elif re.search("14:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["14:00"] += 1
        elif re.search("15:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["15:00"] += 1
        elif re.search("16:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["16:00"] += 1
        elif re.search("17:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["17:00"] += 1
        elif re.search("18:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["18:00"] += 1
        elif re.search("19:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["19:00"] += 1
        elif re.search("20:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["20:00"] += 1
        elif re.search("21:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["21:00"] += 1
        elif re.search("22:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["22:00"] += 1
        elif re.search("23:", date, re.IGNORECASE):
            number_of_appearances_a_given_day[day_of_week]["23:00"] += 1
    return number_of_appearances_a_given_day

df_spot = pd.read_excel(path.filtered_data_from_webpage_spot_excel)
df_futures = pd.read_excel(path.filtered_data_from_webpage_futures_excel)
df_others = pd.read_excel(path.filtered_data_from_webpage_others_excel)
print("df_spot = " + str(check_hour_probability(df_spot)))
print("df_futures = " + str(check_hour_probability(df_futures)))
print("df_others = " + str(check_hour_probability(df_others)))