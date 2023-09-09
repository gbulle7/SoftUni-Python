player1_seconds = int(input())
player2_seconds = int(input())
player3_seconds = int(input())
total_time = player1_seconds + player2_seconds + player3_seconds
minutes = total_time // 60
seconds = total_time % 60
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
