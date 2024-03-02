# def validate_password(passwd):
#     valid = True
#     if not 6 <= len(passwd) <= 10:
#         valid = False
#         print('Password must be between 6 and 10 characters')
#     if not passwd.isalnum():
#         valid = False
#         print('Password must consist only of letters and digits')
#     if len([char for char in passwd if char.isdigit()]) < 2:
#         valid = False
#         print('Password must have at least 2 digits')
#     if valid:
#         print('Password is valid')
#
# password = input()
# validate_password(password)

def password_validator(password):
    errors = []

    if not 6 <= len(password) <= 10:
        errors.append("Password must be between 6 and 10 characters")

    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")

    if sum(char.isdigit() for char in password) < 2:
        errors.append("Password must have at least 2 digits")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid")


user_password = input()
password_validator(user_password)


# RegEx
# import re
#
#
# class PasswordValidator:
#     def __init__(self, password):
#         self.password = password
#         self.errors = []
#
#     def is_valid(self):
#         self._check_length()
#         self._check_alphanumeric()
#         self._check_digit_count()
#
#         if self.errors:
#             return False
#         return True
#
#     def _check_length(self):
#         if not 6 <= len(self.password) <= 10:
#             self.errors.append("Password must be between 6 and 10 characters")
#
#     def _check_alphanumeric(self):
#         if not re.match("^[a-zA-Z0-9]+$", self.password):
#             self.errors.append("Password must consist only of letters and digits")
#
#     def _check_digit_count(self):
#         if sum(char.isdigit() for char in self.password) < 2:
#             self.errors.append("Password must have at least 2 digits")
#
#     def get_errors(self):
#         return self.errors
#
#
# user_password = input()
# validator = PasswordValidator(user_password)
#
# if validator.is_valid():
#     print("Password is valid")
# else:
#     for error in validator.get_errors():
#         print(error)

