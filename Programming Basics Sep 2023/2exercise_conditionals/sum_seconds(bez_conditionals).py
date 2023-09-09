player1_seconds = int(input())
player2_seconds = int(input())
player3_seconds = int(input())
total_time = (player1_seconds + player2_seconds + player3_seconds) / 60
remaining_seconds = (total_time - int(total_time)) * 60
remaining_minutes = int(total_time)
print(f'{remaining_minutes}:{remaining_seconds:02.0f}')     # 02.0f = 02d
