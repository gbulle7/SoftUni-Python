username = input()
password = input()
log_in_data = input()

while log_in_data != password:
    log_in_data = input()
print(f'Welcome {username}!')  # can use else:
