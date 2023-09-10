exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())
time_exam_minutes = exam_hour * 60 + exam_minute
time_arrival_minutes = arrival_hour * 60 + arrival_minute

if time_arrival_minutes > time_exam_minutes:
    print('Late')
elif time_exam_minutes - 30 <= time_arrival_minutes <= time_exam_minutes:
    print('On time')
elif time_exam_minutes - 30 > time_arrival_minutes:  # else:
    print('Early')

difference_minutes = abs(time_arrival_minutes - time_exam_minutes)
hours = difference_minutes // 60
minutes = difference_minutes % 60

if difference_minutes < 60:
    if time_arrival_minutes < time_exam_minutes:
        print(f'{minutes} minutes before the start')
    elif time_arrival_minutes > time_exam_minutes:
        print(f'{minutes} minutes after the start')
elif difference_minutes >= 60:  # else:
    difference_minutes %= 60
    if time_arrival_minutes < time_exam_minutes:
        print(f'{hours}:{minutes:02d} hours before the start')
    elif time_arrival_minutes > time_exam_minutes:
        print(f'{hours}:{minutes:02d} hours after the start')
