import datetime as dt

from pprint import pprint


def sum_time(time_1, time_2):
    hours = time_1.hour + time_2.hour
    minutes = time_1.minute + time_2.minute
    if minutes >= 60:
        hours += minutes // 60
        minutes = minutes % 60
    return dt.time(hours, minutes)


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

busy_time = []
for item in busy:
    start_busy = dt.time.fromisoformat(item['start'])
    stop_busy = dt.time.fromisoformat(item['stop'])
    busy_time.append((start_busy, stop_busy))

start_time = dt.time.fromisoformat('09:00')
end_time = dt.time.fromisoformat('21:00')
busy_time.sort()
window_for_work = dt.time.fromisoformat('00:30')
windows = []
while start_time < end_time:
    for item in busy_time:
        while start_time < item[0] and item[0] >= sum_time(
                start_time, window_for_work):
            time = sum_time(start_time, window_for_work)
            windows.append((start_time, time))
            start_time = time
        if start_time < end_time:
            start_time = item[1]
        else:
            break
    if start_time < end_time and sum_time(
            start_time, window_for_work) < end_time:
        windows.append((start_time, sum_time(start_time, window_for_work)))
        break

print(f'Количество свободных номерков у доктора - {len(windows)}.')
for start, end in windows:
    pprint(f'{start.strftime("%H:%M")} - {end.strftime("%H:%M")}')
