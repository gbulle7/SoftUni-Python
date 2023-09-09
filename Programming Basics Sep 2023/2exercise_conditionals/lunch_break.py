from math import ceil

serial = input()
time_episode = int(input())
time_lunchbreak = int(input())
time_lunch = time_lunchbreak / 8
time_rest = time_lunchbreak / 4
time_for_watching = time_lunchbreak - time_lunch - time_rest
difference = abs(time_for_watching - time_episode)
if time_for_watching >= time_episode:
    print(f'You have enough time to watch {serial} and left with {ceil(difference)} minutes free time.')
else:
    print(f"You don't have enough time to watch {serial}, you need {ceil(difference)} more minutes.")
