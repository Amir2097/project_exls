import datetime


str_d = '22.04.23'
srt_d2 = '2023-04-24 12:52:58'

# date_time_obj = datetime.datetime.strptime(str_d, '%d.%m.%Y')
dadsa = datetime.datetime.strptime(srt_d2, '%Y-%m-%d')
print(date_time_obj)
print(dadsa)