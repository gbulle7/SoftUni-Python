# first method
username = input("Enter your username: ")
password = input("Enter your password: ")

for _ in range(3):  # Allow three login attempts
    log_in_data = input("Enter login data: ")
    if log_in_data == password:
        print(f'Welcome, {username}!')
        break
    else:
        print("Incorrect login data. Please try again.")
else:
    print("Maximum login attempts reached. Access denied.")

# second method
#username = input("Enter your username: ")
# password = input("Enter your password: ")
#
# max_attempts = 3
# success = False
#
# for attempt in range(max_attempts):
#     log_in_data = input("Enter login data: ")
#     if log_in_data == password:
#         print(f'Welcome, {username}!')
#         success = True
#         break
#     else:
#         print("Incorrect login data. Please try again.")
#
# if not success:
#     print("Maximum login attempts reached. Access denied.")
