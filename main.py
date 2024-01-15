import datetime as dt

from pprint import pprint


busy = [
    {'start': '10:30',
     'stop': '10:50'},
    {'start': '18:40',
     'stop': '18:50'},
    {'start': '14:40',
     'stop': '15:50'},
    {'start': '16:40',
     'stop': '17:20'},
    {'start': '20:05',
     'stop': '20:20'},
]

busy_datetime = []
for item in busy:
    start_time = dt.datetime.strptime(item['start'], '%H:%M').time()
    stop_time = dt.datetime.strptime(item['stop'], '%H:%M').time()
    busy_datetime.append((start_time, stop_time))
pprint(busy_datetime)

start_time = dt.datetime.strptime('09:00', '%H:%M').time()
end_time = dt.datetime.strptime('21:00', '%H:%M').time()
busy_datetime.sort()
window_for_work = dt.datetime.strptime('00:30', '%H:%M').time()
windows = []
while start_time < end_time:
    for item in busy_datetime:
        if start_time < item[0] and item[1] > start_time + window_for_work:
            windows.append((start_time, start_time + window_for_work))
            start_time += window_for_work
        elif start_time < item[0] and item[1] <= start_time + window_for_work:
            start_time = item[1]
        else:
            start_time += window_for_work
            
pprint(windows)